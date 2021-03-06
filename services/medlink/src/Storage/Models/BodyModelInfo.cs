﻿using System.Collections.Generic;

namespace medlink.Storage
{
    public class BodyModelInfo
    {
        public string ModelSeries { get; set; }
        public string Revision { get; set; }
        public string BodyFamilyUUID { get; set; }
        public Dictionary<string, double> ReferenceValues { get; set; }
    }
}