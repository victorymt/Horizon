# Daily publication recovery (2026-10-25)

The Actions workflow page reports: “Workflows are not currently being run on this fork due to the scale of GitHub Actions usage. A repository maintainer can choose to re-enable these.” This is a platform suspension, not an AI request failure or an invalid cron expression. Changing cron alone cannot lift it.

A maintainer must sign in to the repository Actions page, re-enable workflows, and run Daily Horizon Summary on main. Verify both language posts on gh-pages and the subsequent pages-build-deployment run. Do not infer recovery from a successful source commit or skipped run.

The last observed scheduled run is 39722003648 (October 22), with 25 successful AI analyses and zero failures. The published head is 9dfdb5ccb18c009c1dea1a01739be0fbc3902455. No October 23 or 24 runs/posts exist. The October 22 run has no artifacts. The old workflow did not preserve raw inputs or scraper state, and current HN top stories / Reddit hot listings cannot recreate those dates. Historical summaries were therefore not fabricated from today's 48-hour window.

The revised workflow makes three off-hour attempts per UTC day, serializes publication, skips days with both language posts, checks both new outputs before deployment, and preserves raw input and summaries as 90-day artifacts even after analysis failures. No-content runs now fail the output gate instead of silently deploying unchanged docs. The CLI pins the report date before work starts and rejects a historical date for live fetching. News selection is still a rolling 48-hour lookback, not a complete calendar-day archive; delayed scrapes cannot recover items which left current source listings. Artifacts preserve exactly the observed input, not proof of exhaustive source coverage.

AI startup validation and nonzero failure propagation remain enabled. Authentication/all-analysis failures must continue to block deployment. Local validation: 269 tests passed, including authentication regression tests, historical-date rejection, and raw-input preservation after analysis failure.
