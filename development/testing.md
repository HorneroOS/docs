# Testing HorneroOS changes

Choose evidence that matches the risk. A pure documentation edit needs link
and markdown checks; a Shell interaction change needs real input and rendered
evidence; a package or theme change needs to be checked outside the owner's
dotfiles environment.

## Before testing

1. Read the target repository's test instructions and inspect the exact
   changes being tested.
2. Keep test data under a temporary directory or disposable VM. Never archive
   a developer's home directory or apply test configuration to a live host.
3. Disable telemetry or reporting where the test environment supports it.
4. Keep VM/build concurrency within available memory and CPU limits.

## Graphical acceptance

Use the existing [Hornero QA repository](https://github.com/HorneroOS/qa)
when an established scenario covers the behavior. Drive user journeys with
keyboard and pointer input, and use screenshots or recordings to inspect
actual output. Deterministic checks establish acceptance; visual review
explains whether the experience is coherent. Do not treat a command/API call
as proof of a user interaction unless the API itself is under test.

For appearance work, verify that selected theme, mode, Shell palette, GTK,
icons, and wallpaper report the expected state. For Settings work, verify
mouse and keyboard navigation, visible focus, persistence, and recovery from
unavailable dependencies. Package-only claims require a package-faithful
environment without personal dotfiles supplying missing files.

## Evidence and reports

Keep useful evidence with the test run and preserve its provenance. Public
product imagery should be deliberately curated from genuine runtime captures;
debug screenshots and private desktop contents are not public media. Record
the tested revision and environment when those facts affect interpretation.

Follow each repository's CI and test commands. Do not introduce a new test
framework when an existing check can prove the required behavior.
