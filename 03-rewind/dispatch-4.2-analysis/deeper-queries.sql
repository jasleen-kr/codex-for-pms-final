-- outcomes
SELECT responder, CASE WHEN sent_at < TIMESTAMP '2026-08-10' THEN 'before_full_weeks' WHEN sent_at < TIMESTAMP '2026-08-17' THEN 'release_week' ELSE 'after_full_weeks' END AS period, COUNT(*) AS pings, COUNT(*) FILTER (WHERE outcome = 'taken') AS taken, COUNT(*) FILTER (WHERE outcome = 'turned down') AS turned_down, COUNT(*) FILTER (WHERE outcome = 'missed') AS missed FROM rook.pings WHERE sent_at >= TIMESTAMP '2026-06-29' GROUP BY 1,2 ORDER BY 1,2;

-- area_demand
SELECT area, CASE WHEN happened_at < TIMESTAMP '2026-08-10' THEN 'before_full_weeks' WHEN happened_at < TIMESTAMP '2026-08-17' THEN 'release_week' ELSE 'after_full_weeks' END AS period, COUNT(*) AS callouts FROM rook.callouts WHERE happened_at >= TIMESTAMP '2026-06-29' GROUP BY 1,2 ORDER BY 1,2;

-- tickets
SELECT ticket_number, filed_at, filed_by, about_responder, subject, body, status FROM rook.support_tickets WHERE about_responder IN ('Farlight','Meteor Mite','The Undertow','Vesper','The Gale') ORDER BY filed_at,ticket_number;

-- affected_weekly
SELECT DATE_TRUNC('week', sent_at)::date AS week_start, responder, COUNT(*) AS pings, COUNT(*) FILTER (WHERE outcome = 'taken') AS taken, COUNT(*) FILTER (WHERE outcome = 'turned down') AS turned_down, COUNT(*) FILTER (WHERE outcome = 'missed') AS missed FROM rook.pings WHERE responder IN ('Farlight','Meteor Mite','The Undertow','Vesper','The Gale') GROUP BY 1,2 ORDER BY 1,2;
