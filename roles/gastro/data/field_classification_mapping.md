# FIELD CLASSIFICATION — DRAFT MAPPING

## I. Meal Entry (example)

| field                | status    | notes                                 |
| :------------------- | :-------- | :------------------------------------ |
| timestamp            | mandatory | Needed for chronology.                |
| items                | mandatory | Core description of what was eaten.   |
| ingredients          | mandatory | Supports trigger analysis.            |
| metadata             | optional  | Extra context (e.g., "oily").         |
| pre_meal_prokinetics | optional  | Record if taken; null otherwise.      |
| notes                | optional  | Free-text context.                    |

## II. Stool Entry (example)

| field      | status    | notes                                    |
| :--------- | :-------- | :--------------------------------------- |
| timestamp  | mandatory | Needed for chronology.                   |
| type       | mandatory | Bristol 1–7 classification.              |
| metadata   | optional  | Context about urgency, completeness, etc.|
| confidence | optional  | Only for image-based entries.            |
| notes      | optional  | Free-text context.                       |

## III. Digestion Entry (example)

| field      | status    | notes                          |
| :--------- | :-------- | :----------------------------- |
| timestamp  | mandatory | Needed for chronology.         |
| tummy_pain | mandatory | 1–5 numeric severity.          |
| bloating   | mandatory | 1–5 numeric severity.          |
| notes      | optional  | Free-text context.             |

## IV. Mental Entry (example)

| field     | status    | notes                          |
| :-------- | :-------- | :----------------------------- |
| timestamp | mandatory | Needed for chronology.         |
| mood      | mandatory | -2 to 2 numeric scale.         |
| stress    | mandatory | 1–5 numeric severity.          |
| notes     | optional  | Free-text context.             |

