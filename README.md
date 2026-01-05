# Randoro - Random Interval Timer

A random interval timer designed for shadowboxing training and HIIT workouts.

## Why I Built This

The element of surprise is difficult to simulate when training boxing solo. Traditional interval timers are too predictable. In boxing, you need quick reactions and a high punch output. This app provides random configurable boxing cues to practice your skills, reactions, and increase you cardio fitness.

## Features

- **Random intervals** within configurable constraints
- **Multiple rounds** with optional rest periods
- **Warmup/cooldown** optional rounds at the beginning and end
- **Works on mobile** (add to home screen)

## Try It

Live app: [randoro-web.vercel.app](randoro-web.vercel.app)

## Configuration

- **Warmup**: Seconds before first round
- **Rounds**: Number of work/rest cycles
- **Work Duration**: Minutes per round
- **Rest Duration**: Minutes between rounds
- **Intervals**: Number of random pings per round
- **Min Gap**: Minimum seconds between pings
- **Cooldown**: Seconds after final round

## Known Limitations

This is a web app, which has iOS limitations:
- Doesn't work when phone is on silent mode
- Requires screen to stay on
- Audio disables when switching apps

Native mobile app in development to address these.

## Tech Stack

- React
- Deployed on Vercel

## Version

v1.0.0 - MVP with core functionality

## Future Plans

- [ ] Native iOS/Android app
- [ ] Skip to next/previous round
- [ ] Rest-first vs work-first toggle
- [ ] Session history
- [ ] Custom sound options

## License

MIT

---

Built by Diarmuid Brady