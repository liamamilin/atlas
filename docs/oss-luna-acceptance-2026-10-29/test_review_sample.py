import unittest
from review_sample import select_sample, token_cost, validate_review


class ReviewSafeguards(unittest.TestCase):
    def test_all_domains_unique_and_deterministic(self):
        population = [{"repository_id": i, "domain": str(i % 29)} for i in range(55651)]
        selected, strata = select_sample(population)
        self.assertEqual(len(selected), 100)
        self.assertEqual(len({v["repository_id"] for v in selected}), 100)
        self.assertEqual(len(strata), 29)
        self.assertEqual(selected, select_sample(list(reversed(population)))[0])

    def test_fabricated_quote_and_unknown_scenario_cannot_be_evidence(self):
        payload = {"card": {"repository_id": 17}, "sources": [{"id": "s0", "text": "planned ticket routing"}], "scenario_matches": [{"scenario_id": "actual"}]}
        review = {"repository_id": 17, "verdict": "needs_review", "checks": {}, "issues": [{"field": "scenario_match", "scenario_id": "invented", "source_id": "s0", "quote": "implemented ticket routing"}]}
        invalid = validate_review(review, payload)
        self.assertEqual({v["reason"] for v in invalid}, {"quote_not_in_supplied_source", "unknown_scenario"})
        review["repository_id"] = 18
        with self.assertRaises(ValueError):
            validate_review(review, payload)

    def test_cached_input_and_output_are_charged_separately(self):
        usage = {"prompt_tokens": 1000000, "prompt_tokens_details": {"cached_tokens": 200000}, "completion_tokens": 100000}
        self.assertAlmostEqual(token_cost(usage), .132)


if __name__ == "__main__":
    unittest.main()
