-- ============================================================================
-- Hotel Booking EDA - Advanced Analysis
-- Purpose: Advanced exploratory data analysis using CTEs and complex queries
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 1. REVENUE ANALYSIS BY BOOKING STATUS
-- ----------------------------------------------------------------------------
WITH revenue_analysis AS (
    SELECT 
        CASE WHEN is_canceled = 1 THEN 'Canceled' ELSE 'Completed' END AS booking_status,
        COUNT(*) AS total_bookings,
        ROUND(SUM(adr * (stays_in_weekend_nights + stays_in_week_nights)), 2) AS total_revenue,
        ROUND(AVG(adr * (stays_in_weekend_nights + stays_in_week_nights)), 2) AS avg_booking_value
    FROM hotel_bookings
    WHERE adr > 0
    GROUP BY is_canceled
)
SELECT * FROM revenue_analysis;


-- ----------------------------------------------------------------------------
-- 2. BOOKING CHANGES IMPACT ON CANCELLATION
-- ----------------------------------------------------------------------------
WITH booking_changes_analysis AS (
    SELECT 
        CASE 
            WHEN booking_changes = 0 THEN 'No Changes'
            WHEN booking_changes = 1 THEN '1 Change'
            WHEN booking_changes = 2 THEN '2 Changes'
            ELSE '3+ Changes'
        END AS changes_category,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate
    FROM hotel_bookings
    GROUP BY 
        CASE 
            WHEN booking_changes = 0 THEN 'No Changes'
            WHEN booking_changes = 1 THEN '1 Change'
            WHEN booking_changes = 2 THEN '2 Changes'
            ELSE '3+ Changes'
        END
)
SELECT * FROM booking_changes_analysis
ORDER BY 
    CASE changes_category
        WHEN 'No Changes' THEN 1
        WHEN '1 Change' THEN 2
        WHEN '2 Changes' THEN 3
        WHEN '3+ Changes' THEN 4
    END;


-- ----------------------------------------------------------------------------
-- 3. PREVIOUS CANCELLATION HISTORY IMPACT
-- ----------------------------------------------------------------------------
WITH cancellation_history_impact AS (
    SELECT 
        CASE 
            WHEN previous_cancellations = 0 THEN 'No History'
            WHEN previous_cancellations BETWEEN 1 AND 2 THEN '1-2 Cancellations'
            ELSE '3+ Cancellations'
        END AS cancellation_history,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS current_cancellations,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate
    FROM hotel_bookings
    GROUP BY 
        CASE 
            WHEN previous_cancellations = 0 THEN 'No History'
            WHEN previous_cancellations BETWEEN 1 AND 2 THEN '1-2 Cancellations'
            ELSE '3+ Cancellations'
        END
)
SELECT * FROM cancellation_history_impact
ORDER BY cancellation_rate DESC;


-- ----------------------------------------------------------------------------
-- 4. GUEST COMPOSITION ANALYSIS
-- ----------------------------------------------------------------------------
WITH guest_composition AS (
    SELECT 
        adults + COALESCE(children, 0) + COALESCE(babies, 0) AS total_guests,
        CASE 
            WHEN adults = 1 AND COALESCE(children, 0) = 0 AND COALESCE(babies, 0) = 0 THEN 'Solo Traveler'
            WHEN adults = 2 AND COALESCE(children, 0) = 0 AND COALESCE(babies, 0) = 0 THEN 'Couple'
            WHEN COALESCE(children, 0) > 0 OR COALESCE(babies, 0) > 0 THEN 'Family'
            ELSE 'Group'
        END AS guest_type,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate
    FROM hotel_bookings
    GROUP BY 
        adults + COALESCE(children, 0) + COALESCE(babies, 0),
        CASE 
            WHEN adults = 1 AND COALESCE(children, 0) = 0 AND COALESCE(babies, 0) = 0 THEN 'Solo Traveler'
            WHEN adults = 2 AND COALESCE(children, 0) = 0 AND COALESCE(babies, 0) = 0 THEN 'Couple'
            WHEN COALESCE(children, 0) > 0 OR COALESCE(babies, 0) > 0 THEN 'Family'
            ELSE 'Group'
        END
)
SELECT 
    guest_type,
    SUM(total_bookings) AS total_bookings,
    SUM(canceled_bookings) AS canceled_bookings,
    ROUND(AVG(cancellation_rate), 2) AS avg_cancellation_rate
FROM guest_composition
GROUP BY guest_type
ORDER BY total_bookings DESC;


-- ----------------------------------------------------------------------------
-- 5. STAY DURATION PATTERNS
-- ----------------------------------------------------------------------------
WITH stay_duration_analysis AS (
    SELECT 
        stays_in_weekend_nights + stays_in_week_nights AS total_nights,
        CASE 
            WHEN stays_in_weekend_nights + stays_in_week_nights = 1 THEN '1 Night'
            WHEN stays_in_weekend_nights + stays_in_week_nights BETWEEN 2 AND 3 THEN '2-3 Nights'
            WHEN stays_in_weekend_nights + stays_in_week_nights BETWEEN 4 AND 7 THEN '4-7 Nights'
            ELSE '8+ Nights'
        END AS stay_duration,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate,
        ROUND(AVG(adr), 2) AS avg_daily_rate
    FROM hotel_bookings
    GROUP BY 
        stays_in_weekend_nights + stays_in_week_nights,
        CASE 
            WHEN stays_in_weekend_nights + stays_in_week_nights = 1 THEN '1 Night'
            WHEN stays_in_weekend_nights + stays_in_week_nights BETWEEN 2 AND 3 THEN '2-3 Nights'
            WHEN stays_in_weekend_nights + stays_in_week_nights BETWEEN 4 AND 7 THEN '4-7 Nights'
            ELSE '8+ Nights'
        END
)
SELECT 
    stay_duration,
    SUM(total_bookings) AS total_bookings,
    SUM(canceled_bookings) AS canceled_bookings,
    ROUND(AVG(cancellation_rate), 2) AS avg_cancellation_rate,
    ROUND(AVG(avg_daily_rate), 2) AS avg_daily_rate
FROM stay_duration_analysis
GROUP BY stay_duration
ORDER BY 
    CASE stay_duration
        WHEN '1 Night' THEN 1
        WHEN '2-3 Nights' THEN 2
        WHEN '4-7 Nights' THEN 3
        WHEN '8+ Nights' THEN 4
    END;


-- ----------------------------------------------------------------------------
-- 6. MEAL TYPE PREFERENCES AND CANCELLATION
-- ----------------------------------------------------------------------------
WITH meal_analysis AS (
    SELECT 
        meal,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate,
        ROUND(AVG(adr), 2) AS avg_daily_rate
    FROM hotel_bookings
    GROUP BY meal
)
SELECT * FROM meal_analysis
ORDER BY total_bookings DESC;


-- ----------------------------------------------------------------------------
-- 7. DISTRIBUTION CHANNEL EFFECTIVENESS
-- ----------------------------------------------------------------------------
WITH channel_effectiveness AS (
    SELECT 
        distribution_channel,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate,
        ROUND(AVG(adr), 2) AS avg_daily_rate,
        ROUND(SUM(CASE WHEN is_canceled = 0 THEN adr * (stays_in_weekend_nights + stays_in_week_nights) ELSE 0 END), 2) AS total_revenue
    FROM hotel_bookings
    WHERE adr > 0
    GROUP BY distribution_channel
)
SELECT * FROM channel_effectiveness
ORDER BY total_revenue DESC;


-- ----------------------------------------------------------------------------
-- 8. WEEKEND VS WEEKDAY STAY PATTERNS
-- ----------------------------------------------------------------------------
WITH weekend_weekday_analysis AS (
    SELECT 
        CASE 
            WHEN stays_in_weekend_nights > stays_in_week_nights THEN 'Weekend-Heavy'
            WHEN stays_in_week_nights > stays_in_weekend_nights THEN 'Weekday-Heavy'
            ELSE 'Balanced'
        END AS stay_pattern,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate,
        ROUND(AVG(stays_in_weekend_nights), 2) AS avg_weekend_nights,
        ROUND(AVG(stays_in_week_nights), 2) AS avg_week_nights
    FROM hotel_bookings
    WHERE (stays_in_weekend_nights + stays_in_week_nights) > 0
    GROUP BY 
        CASE 
            WHEN stays_in_weekend_nights > stays_in_week_nights THEN 'Weekend-Heavy'
            WHEN stays_in_week_nights > stays_in_weekend_nights THEN 'Weekday-Heavy'
            ELSE 'Balanced'
        END
)
SELECT * FROM weekend_weekday_analysis
ORDER BY total_bookings DESC;


-- ----------------------------------------------------------------------------
-- 9. PARKING SPACE REQUIREMENTS
-- ----------------------------------------------------------------------------
WITH parking_analysis AS (
    SELECT 
        CASE 
            WHEN required_car_parking_spaces = 0 THEN 'No Parking'
            WHEN required_car_parking_spaces = 1 THEN '1 Space'
            ELSE '2+ Spaces'
        END AS parking_category,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate
    FROM hotel_bookings
    GROUP BY 
        CASE 
            WHEN required_car_parking_spaces = 0 THEN 'No Parking'
            WHEN required_car_parking_spaces = 1 THEN '1 Space'
            ELSE '2+ Spaces'
        END
)
SELECT * FROM parking_analysis
ORDER BY total_bookings DESC;


-- ----------------------------------------------------------------------------
-- 10. HIGH-VALUE BOOKING ANALYSIS
-- ----------------------------------------------------------------------------
WITH high_value_bookings AS (
    SELECT 
        CASE 
            WHEN adr * (stays_in_weekend_nights + stays_in_week_nights) < 500 THEN 'Low Value (<$500)'
            WHEN adr * (stays_in_weekend_nights + stays_in_week_nights) BETWEEN 500 AND 1000 THEN 'Medium Value ($500-$1000)'
            ELSE 'High Value (>$1000)'
        END AS booking_value_category,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate,
        ROUND(AVG(adr * (stays_in_weekend_nights + stays_in_week_nights)), 2) AS avg_booking_value
    FROM hotel_bookings
    WHERE adr > 0 AND (stays_in_weekend_nights + stays_in_week_nights) > 0
    GROUP BY 
        CASE 
            WHEN adr * (stays_in_weekend_nights + stays_in_week_nights) < 500 THEN 'Low Value (<$500)'
            WHEN adr * (stays_in_weekend_nights + stays_in_week_nights) BETWEEN 500 AND 1000 THEN 'Medium Value ($500-$1000)'
            ELSE 'High Value (>$1000)'
        END
)
SELECT * FROM high_value_bookings
ORDER BY 
    CASE booking_value_category
        WHEN 'Low Value (<$500)' THEN 1
        WHEN 'Medium Value ($500-$1000)' THEN 2
        WHEN 'High Value (>$1000)' THEN 3
    END;


-- ----------------------------------------------------------------------------
-- 11. YEAR-OVER-YEAR COMPARISON
-- ----------------------------------------------------------------------------
WITH yearly_comparison AS (
    SELECT 
        arrival_date_year AS year,
        COUNT(*) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN 1 ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate,
        ROUND(AVG(adr), 2) AS avg_daily_rate,
        ROUND(AVG(lead_time), 2) AS avg_lead_time
    FROM hotel_bookings
    GROUP BY arrival_date_year
)
SELECT * FROM yearly_comparison
ORDER BY year;


-- ----------------------------------------------------------------------------
-- 12. CANCELLATION RISK FACTORS (COMBINED)
-- ----------------------------------------------------------------------------
WITH risk_factors AS (
    SELECT 
        CASE WHEN lead_time > 180 THEN 1 ELSE 0 END AS long_lead_time,
        CASE WHEN previous_cancellations > 0 THEN 1 ELSE 0 END AS has_cancel_history,
        CASE WHEN total_of_special_requests = 0 THEN 1 ELSE 0 END AS no_special_requests,
        CASE WHEN deposit_type = 'No Deposit' THEN 1 ELSE 0 END AS no_deposit,
        is_canceled,
        COUNT(*) AS booking_count
    FROM hotel_bookings
    GROUP BY 
        CASE WHEN lead_time > 180 THEN 1 ELSE 0 END,
        CASE WHEN previous_cancellations > 0 THEN 1 ELSE 0 END,
        CASE WHEN total_of_special_requests = 0 THEN 1 ELSE 0 END,
        CASE WHEN deposit_type = 'No Deposit' THEN 1 ELSE 0 END,
        is_canceled
),
risk_summary AS (
    SELECT 
        long_lead_time + has_cancel_history + no_special_requests + no_deposit AS risk_score,
        SUM(booking_count) AS total_bookings,
        SUM(CASE WHEN is_canceled = 1 THEN booking_count ELSE 0 END) AS canceled_bookings,
        ROUND(AVG(CASE WHEN is_canceled = 1 THEN 1.0 ELSE 0.0 END) * 100, 2) AS cancellation_rate
    FROM risk_factors
    GROUP BY long_lead_time + has_cancel_history + no_special_requests + no_deposit
)
SELECT 
    CASE risk_score
        WHEN 0 THEN 'Very Low Risk (0 factors)'
        WHEN 1 THEN 'Low Risk (1 factor)'
        WHEN 2 THEN 'Medium Risk (2 factors)'
        WHEN 3 THEN 'High Risk (3 factors)'
        ELSE 'Very High Risk (4 factors)'
    END AS risk_category,
    total_bookings,
    canceled_bookings,
    cancellation_rate
FROM risk_summary
ORDER BY risk_score;
