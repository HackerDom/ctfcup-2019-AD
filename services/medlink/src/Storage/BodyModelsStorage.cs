﻿using System.Collections.Concurrent;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using medlink.Helpers;

namespace medlink.Storage
{
    public class BodyModelsStorage : BaseStorage<BodyModelInfo>, IBodyModelsStorage
    {
        private readonly ISeriesIndex _seriesIndex;
        private readonly ConcurrentBag<BodyIDDTO> _recordsCache;

        public BodyModelsStorage(ISerializer serializer, ISettings settings, ISeriesIndex seriesIndex) : base(
            serializer, settings, settings.BodyDiagnosticFolder)
        {
            _seriesIndex = seriesIndex;
            _recordsCache = new ConcurrentBag<BodyIDDTO>(_seriesIndex.SelectMany(pair => pair.Value.Value.Select(revision =>
                new BodyIDDTO
                {
                    Series = pair.Key,
                    Revision = revision.Key
                })));
        }

        protected override void OnAdd(BodyModelInfo info, string filename)
        {
            if (!_seriesIndex.Contains(info.ModelSeries))
            {
                var set = new ConcurrentDictionary<string, byte>();
                set[info.Revision] = 0;
                
                _seriesIndex.Add($"{info.ModelSeries}", set);
            }
            else
            {
                _seriesIndex.Get(info.ModelSeries)[info.Revision] = 0;
            }

            _recordsCache.Add(new BodyIDDTO
            {
                Series = info.ModelSeries,
                Revision = info.Revision,
            });
        }

        public bool Contains(string series, string revision)
        {
            return _seriesIndex.TryGet(series, out var revisions) && revisions.ContainsKey(revision);
        }

        public bool Contains(string series)
        {
            return _seriesIndex.Contains(series);
        }

        public Task Add(BodyModelInfo info)
        {
            return Add(info, Path.Combine(info.ModelSeries, info.Revision));
        }

        public Task<BodyModelInfo> Get(string series, string revision)
        {
            return Get(Path.Combine(series, revision));
        }

        public IEnumerable<BodyIDDTO> GetAllModels()
        {
            return _recordsCache;
        }
    }
}