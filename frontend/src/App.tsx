
import { useEffect, useState } from 'react'

type DraftScenario = {
  name: string
  draft_year: number
  expansion_teams: string[]
  protected_players_per_team: number
  max_losses_per_existing_team: number
  two_way_players_eligible: boolean
}

export default function App() {
  const [scenario, setScenario] =
    useState<DraftScenario | null>(null)

  const [error, setError] = useState('')

  useEffect(() => {
    const controller = new AbortController()

    fetch('/api/scenarios/default', {
      signal: controller.signal,
    })
      .then(async (response) => {
        if (!response.ok) {
          throw new Error('Backend request failed')
        }
        return response.json() as Promise<DraftScenario>
      })
      .then(setScenario)
      .catch((err: unknown) => {
        if (
          err instanceof Error &&
          err.name === 'AbortError'
        ) {
          return
        }
        setError('Could not connect to the API.')
      })

    return () => controller.abort()
  }, [])

  return (
    <main style={{
      maxWidth: 900,
      margin: '0 auto',
      padding: '64px 24px',
    }}>
      <p>NBA EXPANSION INTELLIGENCE</p>
      <h1>LeagueShift</h1>

      <p>
        Explore how expansion draft rules and
        roster protection decisions could reshape
        the NBA.
      </p>

      <hr />

      <h2>2028 Expansion Scenario</h2>

      {error && <p role="alert">{error}</p>}

      {!scenario && !error && <p>Loading...</p>}

      {scenario && (
        <section>
          <p><strong>{scenario.name}</strong></p>

          <p>
            Expansion teams:{' '}
            {scenario.expansion_teams.join(' & ')}
          </p>

          <p>
            Protected players per team:{' '}
            {scenario.protected_players_per_team}
          </p>

          <p>
            Maximum losses per existing team:{' '}
            {scenario.max_losses_per_existing_team}
          </p>
        </section>
      )}
    </main>
  )
}
