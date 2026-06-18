# Feature Specification: Mood-Based Music Recommendation

## Description

The application recommends songs based on a user's selected mood. The frontend sends the selected mood to the Flask backend, and the backend returns matching song recommendations for display in the UI.

## Users

- Listeners who want quick music recommendations for a selected mood.
- Developers maintaining the backend recommendation API and frontend recommendation flow.

## API Contract

- Method: `POST`
- Endpoint: `/recommend`
- Request body:

```json
{
  "mood": "happy"
}
```

- Success response: `200 OK`

```json
{
  "songs": [
    {
      "title": "Song title",
      "artist": "Artist name",
      "link": "https://example.com/song"
    }
  ]
}
```

- Error responses:
  - `400 Bad Request` when mood input is missing or invalid.
  - Existing error response format must remain stable for current clients.

## Requirements

- The frontend must request recommendations from `/recommend`.
- The backend must accept mood input from the POST request body.
- The backend must map supported moods to song recommendations.
- Each recommended song must include `title`, `artist`, and `link`.
- Existing Flask routes and frontend API behavior must remain stable.

## Acceptance Criteria

- A valid mood returns a list of matching songs.
- Missing mood input returns a validation error.
- The frontend renders returned song titles, artists, and links.
- No deployed behavior changes are introduced by this specification.
