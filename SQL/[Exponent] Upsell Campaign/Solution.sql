-- https://www.tryexponent.com/practice/prepare/upsell-campaigns
-- 1
SELECT AVG(EXTRACT(DAY FROM (date_end - date_start))) AS average_duration_days
FROM campaign;

-- 2
SELECT c.upsell_campaign_id,
       COUNT(DISTINCT t.user_id) AS eligible_users_with_purchase
FROM campaign c
JOIN "transaction" t ON t.transaction_date BETWEEN c.date_start AND c.date_end
JOIN "user" u ON t.user_id = u.user_id
WHERE u.is_eligible_for_upsell_campaign = TRUE
GROUP BY c.upsell_campaign_id;

-- 3
WITH dur_cmp_cte AS (
    SELECT trx.product_id
    , SUM(trx.quantity) AS quantity_during_campaign
    FROM campaign cmp
    JOIN "transaction" trx ON trx.transaction_date BETWEEN cmp.date_start AND cmp.date_end
    GROUP BY 1
)
, not_dur_cmp_cte AS (
    SELECT trx.product_id
    , SUM(trx.quantity) AS quantity_outside_campaign
    FROM "transaction" trx
    WHERE NOT EXISTS(
            SELECT 1
            FROM campaign cmp
            WHERE trx.transaction_date BETWEEN cmp.date_start AND cmp.date_end
            )
    GROUP BY 1
)
SELECT
COALESCE(dcc.product_id, ndcc.product_id) AS product_id
, dcc.quantity_during_campaign
, ndcc.quantity_outside_campaign
, dcc.quantity_during_campaign - ndcc.quantity_outside_campaign AS quantity_increase
, DENSE_RANK() OVER(ORDER BY dcc.quantity_during_campaign - ndcc.quantity_outside_campaign DESC) AS "rank"
FROM dur_cmp_cte dcc
FULL OUTER JOIN not_dur_cmp_cte ndcc ON ndcc.product_id = dcc.product_id
ORDER BY 5
;