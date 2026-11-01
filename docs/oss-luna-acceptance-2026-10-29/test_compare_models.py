import unittest
from compare_models import select_pairs, citation_metrics


class PairedComparisonSafeguards(unittest.TestCase):
    def test_fifty_identical_case_pairs_cover_all_domains_and_calibration(self):
        items = [{"repository_id": i, "domain": str(i % 29)} for i in range(100)]
        manifest = {"projects": items, "strata": {str(i): {"population": 1000 + i} for i in range(29)}}
        selected = select_pairs(manifest, [1, 2, 3, 4, 5, 6])
        self.assertEqual(len(selected), 50)
        self.assertEqual(len({v["repository_id"] for v in selected}), 50)
        self.assertEqual(len({v["domain"] for v in selected}), 29)
        self.assertTrue({1, 2, 3, 4, 5, 6} <= {v["repository_id"] for v in selected})
        self.assertEqual(selected, select_pairs({**manifest, "projects": list(reversed(items))}, [1, 2, 3, 4, 5, 6]))

    def test_whitespace_is_distinguished_from_invented_evidence(self):
        payload = {"sources": [{"id": "s0", "text": "planned\nfeatures"}]}
        result = {"review": {"issues": [{"source_id": "s0", "quote": "planned features"}, {"source_id": "s0", "quote": "implemented features"}]}}
        self.assertEqual(citation_metrics(result, payload), {"whitespace_only_difference": 1, "not_found_in_source": 1})

    def test_inserted_omission_marker_is_not_official_evidence(self):
        payload = {"sources": [{"id": "s0", "text": "[ARCHIVE TEXT OMITTED]"}]}
        result = {"review": {"issues": [{"source_id": "s0", "quote": "[ARCHIVE TEXT OMITTED]"}]}}
        self.assertEqual(citation_metrics(result, payload), {"truncation_marker_not_official_evidence": 1})


if __name__ == "__main__":
    unittest.main()
