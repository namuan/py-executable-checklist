# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 1.4.0 (2023-02-04)

### Feat

- Trim lines to reduce screen space used

## 1.3.1 (2023-01-01)

### Refactor

- Remove unnecessary files

## 1.3.0 (2023-01-01)

### Feat

- Use proper way to identify verbosity for logging

### Refactor

- ward -> pytest

## 1.2.0 (2022-05-26)

### Feat

- Support defining sub(child) workflows from within a step definition

## 1.1.0 (2022-05-26)

### Feat

- Ignore any private variables defined inside step definition

## 1.0.0 (2022-02-06)

### Feat

- Allow steps to return data instead of setting a global variable

### BREAKING CHANGE

- Removed run(...) as it is replaced with execute()

## 0.11.0 (2022-02-06)

### Feat

- Allow steps to return data for updating context

## 0.10.2 (2022-02-06)

### Fix

- Update documentation

## 0.10.1 (2021-12-26)

### Fix

- Using PAT for running update dependencies workflow

## 0.10.0 (2021-12-26)

### Feat

- Added command to initialise a new project

## 0.9.0 (2021-12-25)

### Feat

- Add support for running workflow steps

## 0.8.3 (2021-12-25)

### Fix

- Remove jekyll theme

## 0.8.2 (2021-12-25)

### Fix

- Using latest version and added job dependency

## 0.8.1 (2021-12-25)

### Fix

- Using correct property name

## 0.8.0 (2021-12-25)

### Feat

- Using support GH action

## 0.7.0 (2021-12-25)

### Feat

- Using personal token so that GH can trigger another workflow

## 0.6.0 (2021-12-25)

### Feat

- Auto publish release if version is bumped

## 0.5.0 (2021-12-25)

### Feat

- Rename project

## 0.4.0 (2021-12-25)

### Feat

- Allow bumping version after build is successful

### Fix

- Use set-output instead of set-env (deprecated from GH actions)

## 0.3.0 (2021-12-25)

### Feat

- Add capability to wait for a user action

## 0.2.0 (2021-12-25)

### Feat

- Add capability to send notification

## 0.1.0 (2021-12-25)

### Feat

- Add command to build package locally
- Ability to run shell commands
- Add make command for running tests
- Initial commit
