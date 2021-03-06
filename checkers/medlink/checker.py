#!/usr/bin/env python3.7

import random
import uuid

from client import *

from gornilo import CheckRequest, Verdict, Checker, PutRequest, GetRequest

checker = Checker()


@checker.define_check
def check_service(request: CheckRequest) -> Verdict:
    try:
        vendor = register_vendor(request.hostname)

        vendor_session = vendor["session"]
        v_token = vendor["vendorToken"]
        body_model = utils.get_body_model()
        put_body(request.hostname, vendor_session, body_model, v_token)
        bodies = get_supported_bodies(request.hostname, vendor_session)

        if {"series": body_model["modelSeries"], "revision": body_model["revision"]} not in bodies:
            return Verdict.MUMBLE("GET /api/bodymodels not contains %s revision %s" % (body_model["modelSeries"],
                                                                                         body_model["revision"]))

        received = get_body(request.hostname, vendor_session, body_model["modelSeries"], body_model["revision"], v_token)

        if body_model["modelSeries"] != received["modelSeries"]:
            return Verdict.MUMBLE("GET api/bodymodel unknown modelSeries")

        for key in body_model["referenceValues"].keys():
            if key not in received["referenceValues"] or body_model["referenceValues"][key] != received["referenceValues"][
                key]:
                return Verdict.MUMBLE("GET api/bodymodel unknown referenceValues")

        template = get_model_template(request.hostname, vendor_session, body_model["modelSeries"], body_model["revision"])

        lower_temp = {v.lower(): v for v in template}

        for key in body_model["referenceValues"].keys():
            if key not in lower_temp:
                return Verdict.MUMBLE("GET api/template unknown values")

        user = register_user(request.hostname)
        user_session = user["session"]
        user_model = {"series": body_model["modelSeries"], "revision": body_model["revision"]}
        template = get_model_template(request.hostname, user_session, user_model["series"], user_model["revision"])

        telemetry = {
            "bodyID": utils.get_bodyid(),
            "bodyModelSeries": user_model["series"],
            "bodyRevision": user_model["revision"],
            "hardwareTelemetry": {}
        }

        for parameter in template:
            telemetry["hardwareTelemetry"][parameter] = random.randrange(0, 100)

        put_telemetry(request.hostname, user_session, telemetry)
        r_telemetry = get_telemetry(request.hostname, user_session)

        if telemetry["bodyID"] != r_telemetry["bodyID"]:
            return Verdict.MUMBLE("GET api/telemetry bad bodyId")

        for key in r_telemetry["hardwareTelemetry"].keys():
            if r_telemetry["hardwareTelemetry"][key] != telemetry["hardwareTelemetry"][key]:
                return Verdict.MUMBLE("GET api/telemetry bad hardwareTelemetry")

        r_check = health_check(request.hostname, user_session)

        for key in r_check["checkResults"].keys():
            if key not in template:
                return Verdict.MUMBLE("GET api/telemetry bad checkResults")

        return Verdict.OK()
    except HTTPException as e:
        return e.verdict


@checker.define_put(vuln_num=1, vuln_rate=1)
def put_flag_into_the_service(request: PutRequest) -> Verdict:
    try:
        vendor = register_vendor(request.hostname)
        vendor_session = vendor["session"]
        v_token = vendor["vendorToken"]
        body_model = utils.get_body_model()
        body_model["BodyFamilyUUID"] = str(uuid.uuid4())
        put_body(request.hostname, vendor_session, body_model, v_token)

        user_session = vendor["session"]

        user_model = {"series": body_model["modelSeries"], "revision": body_model["revision"]}
        template = get_model_template(request.hostname, user_session, user_model["series"], body_model["revision"])

        telemetry = {
            "bodyID": request.flag,
            "bodyModelSeries": user_model["series"],
            "bodyRevision": user_model["revision"],
            "hardwareTelemetry": {}
        }

        for parameter in template:
            telemetry["hardwareTelemetry"][parameter] = random.randrange(0, 100)

        put_telemetry(request.hostname, user_session, telemetry)
        return Verdict.OK(json.dumps({"session": user_session}))
    except HTTPException as e:
        return e.verdict


@checker.define_put(vuln_num=2, vuln_rate=1)
def put_flag_into_the_service(request: PutRequest) -> Verdict:
    try:
        vendor = register_vendor(request.hostname)
        vendor_session = vendor["session"]
        v_token = vendor["vendorToken"]
        body_model = utils.get_body_model()
        body_model["BodyFamilyUUID"] = request.flag
        put_body(request.hostname, vendor_session, body_model, v_token)

        return Verdict.OK(json.dumps({"session": vendor_session,
                                      "vendorToken": v_token,
                                      "series": body_model["modelSeries"],
                                      "revision": body_model["revision"]}))
    except HTTPException as e:
        return e.verdict


@checker.define_get(vuln_num=1)
def get_flag_from_the_service(request: GetRequest) -> Verdict:
    try:
        r_telemetry = get_telemetry(request.hostname, json.loads(request.flag_id)["session"])

        if r_telemetry["bodyID"] != request.flag:
            return Verdict.CORRUPT("flag corrupted")

        return Verdict.OK()
    except HTTPException as e:
        return e.verdict


@checker.define_get(vuln_num=2)
def get_flag_from_the_service(request: GetRequest) -> Verdict:
    try:
        user = json.loads(request.flag_id)
        r_telemetry = get_body(request.hostname, user["session"], user["series"], user["revision"], user["vendorToken"])

        if r_telemetry["bodyFamilyUUID"] != request.flag:
           return Verdict.CORRUPT("flag corrupted")

        return Verdict.OK()
    except HTTPException as e:
        return e.verdict


if __name__ == '__main__':
    checker.run()
