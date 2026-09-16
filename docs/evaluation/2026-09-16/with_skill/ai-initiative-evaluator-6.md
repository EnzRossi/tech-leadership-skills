# AI initiative decision: Weekly demand forecasts

Inventory sponsor · Evidence: your description of the analyst's experiment

## Recommendation

**Confidence: High that the reported accuracy cannot justify investment; medium on eventual forecasting value.**

Fund a bounded forecasting-data and baseline validation exercise, not an LLM agent. The post-forecast column leaks future information, and a random split does not credibly simulate forecasts made over time. Rebuild the evaluation using only inputs available when planners actually decide. Structured demand prediction is a candidate for statistical forecasting or predictive ML; no need for language generation or agent orchestration has been established.

## Decisive evidence

You report SKU/store/week sales, stockouts and promotions. These are plausible forecasting inputs, but sales during stockouts understate unmet demand, and planned promotions must be distinguished from details known only after the forecast. Labels and feature timestamps need inspection before model comparisons.

The analyst's excellent random-split result includes a future-populated column. It is not valid evidence of deployable performance. Removing that column alone is insufficient if other aggregates or transformations use future weeks or related records improperly.

Forecasts advise planners only, which bounds automatic action but does not remove costly ordering errors. Planners need enough time, context and authority to challenge a bad forecast. Current forecast quality, decision horizon, actual inventory consequences and data permission are Unknown.

## Good enough for the next stage

Define the forecast origin and horizons with planners. Reconstruct historical inputs as of each origin, fit transformations only on training data, and use rolling temporal backtests plus a final untouched later period. Test normal demand separately from promotions, sparse or new SKUs and stockout periods. Choose whether the target is observed sales or estimated unconstrained demand and document limitations.

Compare seasonal-naive and simple statistical forecasts with current planner forecasts and a suitable predictive ML candidate. No LLM comparison is necessary unless a specific interpretive step earns its place. Qualified inventory analysts should adjudicate problematic labels; use reproducible numeric scoring alongside operational judgment.

Measure error and directional bias across relevant slices, then inventory consequences such as shortage and excess-stock exposure where a credible simulation is possible. Avoid an overall average dominated by high-volume items. Set acceptance thresholds from baseline performance and planner cost trade-offs, not a generic accuracy percentage. Measure planner review time and overrides as part of net value.

## Next commitment

Proposed owner: inventory analytics with a planning lead. Cap initial work at repairing the time-aware dataset and delivering reproducible baseline backtests. Advance to a review-only pilot only if the held-out result improves agreed operational measures and permitted data, ownership and fallback are established. Stop/rework if accuracy disappears without leakage or demand labels cannot support the intended decision. Preserve existing planning throughout.

## What could change the recommendation

The strongest counterargument is that future-known business plans genuinely provide valuable signal. Use them only if archived evidence proves they were available at each forecast origin. Clarify the forecast horizon, baseline planning performance and timing of promotion data; those facts determine whether a forecasting investment is worthwhile and how to evaluate it.
