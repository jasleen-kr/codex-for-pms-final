-- tickets
SELECT ticket_number, filed_at, filed_by, about_responder, subject, body, status FROM rook.support_tickets ORDER BY filed_at, ticket_number;

-- daily
SELECT sent_at::date AS date, COUNT(*) AS pings, COUNT(*) FILTER (WHERE outcome = 'taken') AS taken, COUNT(*) FILTER (WHERE outcome = 'turned down') AS turned_down, COUNT(*) FILTER (WHERE outcome = 'missed') AS missed FROM rook.pings WHERE sent_at >= TIMESTAMP '2026-06-01' GROUP BY 1 ORDER BY 1;

-- Rolling count checks: tickets with numeric claims within covered ping dates
SELECT t.ticket_number, t.filed_at, t.about_responder, COUNT(p.sent_at) AS recorded_pings_last_7_days FROM rook.support_tickets t LEFT JOIN rook.pings p ON p.responder = t.about_responder AND p.sent_at >= t.filed_at - INTERVAL '7 days' AND p.sent_at < t.filed_at WHERE t.ticket_number IN (3071,3073,3080,3081,3083,3086,3089,3097,3098,3104,3108,3114,3118,3129,3135) GROUP BY t.ticket_number,t.filed_at,t.about_responder ORDER BY t.ticket_number;
