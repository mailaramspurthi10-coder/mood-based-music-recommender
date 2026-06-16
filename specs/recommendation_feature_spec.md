# Feature Specification: Mood-Based Recommendation

## Feature
Title: Mood-based song recommendations
Owner: Product Team
Date: 2026-06-16

## Background
The web app recommends songs based on a user's selected mood. The backend exposes endpoints that return a list of songs for a given mood and returns a 404 error when the mood is not recognized.

## Acceptance Criteria
- The endpoint `/recommend/<mood>` returns a JSON list of songs for valid moods.
- The endpoint is case-insensitive for mood input.
- Invalid moods return a 404 error with an error message.

## Scenarios
### Scenario 1: Valid mood returns recommendations
- Given a mood value of `happy`
- When the user requests `/recommend/happy`
- Then the API returns a 200 response
- And the response body contains a list of song objects with `title`, `artist`, and `link`

### Scenario 2: Invalid mood returns 404
- Given a mood value of `unknown`
- When the user requests `/recommend/unknown`
- Then the API returns a 404 response
- And the response body contains `{"error": "Mood not found"}`
