-- coverage
SELECT MIN(sent_at) AS first_ping, MAX(sent_at) AS last_ping, COUNT(*) AS pings, COUNT(DISTINCT responder) AS responders FROM rook.pings WHERE sent_at >= TIMESTAMP '2026-06-01';

-- zero_weekly
WITH weeks AS (SELECT generate_series(DATE '2026-06-29', DATE '2026-08-31', INTERVAL '1 week')::date AS week_start), counts AS (SELECT DATE_TRUNC('week', sent_at)::date AS week_start, responder, COUNT(*) AS pings, COUNT(*) FILTER (WHERE outcome = 'taken') AS taken FROM rook.pings WHERE sent_at >= TIMESTAMP '2026-06-01' GROUP BY 1, 2) SELECT w.week_start, r.name AS responder, COALESCE(c.pings, 0) AS pings, COALESCE(c.taken, 0) AS taken FROM weeks w CROSS JOIN rook.responders r LEFT JOIN counts c ON c.week_start = w.week_start AND c.responder = r.name ORDER BY 1, 2;

-- split_rows
SELECT DATE_TRUNC('week', sent_at)::date AS week_start, CASE WHEN sent_at < TIMESTAMP '2026-08-12' THEN 'before' WHEN sent_at < TIMESTAMP '2026-08-13' THEN 'release_day' ELSE 'after' END AS period, responder, COUNT(*) AS pings, COUNT(*) FILTER (WHERE outcome = 'taken') AS taken FROM rook.pings WHERE sent_at >= TIMESTAMP '2026-06-01' GROUP BY 1, 2, 3 ORDER BY 1, 2, 3;

-- periods
SELECT CASE WHEN sent_at < TIMESTAMP '2026-08-12' THEN 'before' WHEN sent_at < TIMESTAMP '2026-08-13' THEN 'release_day' ELSE 'after' END AS period, COUNT(*) AS pings, COUNT(*) FILTER (WHERE outcome = 'taken') AS taken, COUNT(*) FILTER (WHERE outcome = 'turned down') AS turned_down, COUNT(*) FILTER (WHERE outcome = 'missed') AS missed FROM rook.pings WHERE sent_at >= TIMESTAMP '2026-06-01' GROUP BY 1 ORDER BY 1;

-- raw_1
SELECT callout_number, responder, sent_at, outcome FROM rook.pings WHERE sent_at >= TIMESTAMP '2026-06-01' ORDER BY sent_at, callout_number, responder, outcome LIMIT 900;

-- raw_2
SELECT callout_number, responder, sent_at, outcome FROM rook.pings WHERE sent_at >= TIMESTAMP '2026-06-01' ORDER BY sent_at, callout_number, responder, outcome LIMIT 900 OFFSET 900;

