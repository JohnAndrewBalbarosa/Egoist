# Egoist

## Overview

Megarepository containing portfolio of projects across academics, competitive programming, and software experiments.

Repository: [JohnAndrewBalbarosa/Egoist](https://github.com/JohnAndrewBalbarosa/Egoist)

## Problem and Goal

**Problem.** Academic exercises, competitive-programming solutions, graphics work, mobile experiments, and personal projects become difficult to browse when scattered across repositories.

**Goal.** Keep a structured megarepository that preserves source history and groups work by learning domain.

## System Design

- `academics/`: coursework implementations.
- `competitiveProgramming/`: algorithm/problem-solving solutions.
- `gameDevelopment/`, `mobileProgramming/`, `visualGraphics/`: domain experiments.
- `personalProject/`: standalone personal tools; root CMake supports compatible C/C++ targets.

## Setup and Usage

```bash
cmake -S . -B build
cmake --build build

# Individual subprojects may have their own requirements;
# inspect the target directory before running it.
```

## Evaluation Method

- Define the project task and expected behavior.
- Run representative examples or user flows.
- Record correctness, speed, reliability, usability, and failure cases.

## Results

- No validated quantitative results are published yet.
- Current README status: implementation and usage are documented before formal measurement.

## Interpretation

- The project can be described as implemented or in progress, but impact claims should stay limited until measurements are collected.
- Use the evaluation plan below to turn the project into resume-ready, evidence-backed work.

## Limitations

- Results should only be treated as validated when this README includes the dataset, sample size, metric definition, and reproduction steps.
- Any AI-generated, OCR-based, scraped, or heuristic output requires manual review before being used as ground truth.
- Environment-dependent measurements such as latency, memory use, browser behavior, and API reliability should be re-measured on the target machine.

## Recommendations and Future Work

- Add a small benchmark or validation dataset.
- Report sample size, success rate, error rate, and runtime where applicable.
- Add screenshots, logs, or exported reports that support the measured results.

## Documentation Standard

This README follows a technical-project structure: overview, goal, system design, setup, evaluation method, results, interpretation, limitations, and recommendations. Update the Results section whenever new measurements are available so project claims stay evidence-backed.
