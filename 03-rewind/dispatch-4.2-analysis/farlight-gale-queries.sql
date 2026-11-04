-- weekly
WITH weeks AS (SELECT generate_series(DATE '2026-06-29', DATE '2026-08-31', INTERVAL '1 week')::date AS week_start), people AS (SELECT name FROM rook.responders WHERE name IN ('Farlight','The Gale')), counts AS (SELECT DATE_TRUNC('week',sent_at)::date AS week_start, responder, COUNT(*) AS pings, COUNT(*) FILTER (WHERE outcome='taken') AS taken, COUNT(*) FILTER (WHERE outcome='turned down') AS turned_down, COUNT(*) FILTER (WHERE outcome='missed') AS missed FROM rook.pings WHERE responder IN ('Farlight','The Gale') AND sent_at >= TIMESTAMP '2026-06-01' GROUP BY 1,2) SELECT w.week_start, p.name AS responder, COALESCE(c.pings,0) AS pings, COALESCE(c.taken,0) AS taken, COALESCE(c.turned_down,0) AS turned_down, COALESCE(c.missed,0) AS missed FROM weeks w CROSS JOIN people p LEFT JOIN counts c ON c.week_start=w.week_start AND c.responder=p.name ORDER BY 1,2;

-- demand
SELECT area, CASE WHEN happened_at < TIMESTAMP '2026-08-10' THEN 'before' WHEN happened_at < TIMESTAMP '2026-08-17' THEN 'mixed' ELSE 'after' END AS period, COUNT(*) AS callouts FROM rook.callouts WHERE happened_at >= TIMESTAMP '2026-06-29' AND area IN ('Uptown','Eastgate') GROUP BY 1,2 ORDER BY 1,2;

-- responders
SELECT name, handler, area FROM rook.responders WHERE name IN ('Farlight','The Gale') ORDER BY name;
