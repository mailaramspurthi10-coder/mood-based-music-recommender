# Project Constitution

## Core Rules

- Keep code style consistent with the surrounding file and existing project conventions.
- Prefer small, focused changes with clear names and simple control flow.
- Keep backend, frontend, and test changes aligned with the feature specification.
- Do not introduce secrets, hard-coded API keys, or provider-specific credentials.

## API Stability

- The backend Flask API must remain stable for existing clients.
- The frontend must consume the `/recommend` endpoint for music recommendations.
- No breaking API changes are allowed unless the API contract, specs, tests, and documentation are updated together.
- Changes to request or response formats must include migration notes in the related spec.

## Feature Development

- Every feature should begin with a spec in `specs/`.
- Plans and tasks should reference the spec they implement.
- Acceptance criteria must be testable before implementation begins.
