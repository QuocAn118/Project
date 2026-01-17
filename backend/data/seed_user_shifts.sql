-- Seed data for user_shifts table (staff shift assignments)
INSERT INTO user_shifts (user_id, shift_id, date, status) VALUES
(5, 1, '2026-01-20', 'scheduled'),
(5, 2, '2026-01-21', 'scheduled'),
(5, 3, '2026-01-22', 'completed'),
(6, 4, '2026-01-20', 'scheduled'),
(6, 5, '2026-01-21', 'scheduled'),
(6, 6, '2026-01-22', 'scheduled'),
(7, 7, '2026-01-20', 'scheduled'),
(7, 8, '2026-01-21', 'completed'),
(7, 9, '2026-01-22', 'scheduled'),
(8, 1, '2026-01-20', 'scheduled'),
(8, 2, '2026-01-21', 'cancelled'),
(8, 3, '2026-01-22', 'scheduled'),
(9, 4, '2026-01-20', 'scheduled'),
(9, 5, '2026-01-21', 'scheduled'),
(9, 6, '2026-01-22', 'completed');
