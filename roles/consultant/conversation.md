# Architecture Consultation Request

## Context
I need your expertise as a software architecture consultant to help solve a technical challenge in our project. Please explore multiple solution approaches with their trade-offs before making a recommendation.

## Problem Description
[DESCRIBE YOUR SPECIFIC CHALLENGE HERE]

## Current System Context
- **Technology Stack**: [Current technologies used]
- **Architecture Style**: [Monolith/Microservices/etc]
- **Team Size**: [Number of developers]
- **Performance Requirements**: [Specific metrics if known]
- **Timeline**: [Any deadline constraints]

## Specific Challenges
1. [Primary challenge]
2. [Secondary challenge]
3. [Any additional considerations]

## Constraints
- **Technical**: [Any technical limitations]
- **Resources**: [Team/time/budget constraints]
- **Integration**: [Existing systems to work with]
- **Compliance**: [Any regulatory requirements]

## Success Criteria
What would make this solution successful:
- [Specific measurable outcome]
- [Another success metric]
- [User experience goal]

## Questions for You
I'm particularly interested in:
1. What are the different architectural approaches we could take?
2. What are the trade-offs between complexity and functionality?
3. How can we ensure scalability for future growth?
4. What risks should we be aware of?

## Additional Context
[Any other relevant information about the project, team capabilities, or business requirements]

Please explore multiple solutions and help me understand the best path forward for our specific situation. I'm open to both conventional and innovative approaches.
```

### Example Consultant Conversation Starter:

```
# Architecture Consultation Request

## Context
I need your expertise as a software architecture consultant to help solve a technical challenge in our project. Please explore multiple solution approaches with their trade-offs before making a recommendation.

## Problem Description
We're building a trading analysis system that needs to perform real-time pattern detection on price data. Currently, we receive price updates via webhooks every second, but we need to detect complex patterns (like head-and-shoulders, triangles, etc.) that require analyzing the last 20-50 candles of data. 

## Current System Context
- **Technology Stack**: Python, Streamlit, PostgreSQL, Redis
- **Architecture Style**: Modular monolith with component-based structure
- **Team Size**: 3 developers
- **Performance Requirements**: Must process updates within 100ms
- **Timeline**: Need MVP in 4 weeks

## Specific Challenges
1. Real-time webhook only provides current candle, not historical data
2. Pattern detection algorithms are computationally expensive
3. Need to maintain state between webhook calls
4. Must work within Streamlit's stateless architecture

## Constraints
- **Technical**: Cannot modify the webhook data structure
- **Resources**: Limited to current team, no additional hires
- **Integration**: Must work with existing position management system
- **Compliance**: No external API calls for data storage (security requirement)

## Success Criteria
What would make this solution successful:
- Pattern detection completes within 100ms of receiving data
- Accurately identifies at least 5 common trading patterns
- Scales to handle 50+ concurrent symbol analysis
- Maintains pattern history for backtesting

## Questions for You
I'm particularly interested in:
1. Should we pre-compute patterns or calculate in real-time?
2. What's the best way to maintain historical data in our stateless architecture?
3. How can we optimize pattern detection algorithms for speed?
4. Should we consider moving pattern detection to a separate service?

Please explore multiple solutions and help me understand the best path forward for our specific situation. I'm open to both conventional and innovative approaches.