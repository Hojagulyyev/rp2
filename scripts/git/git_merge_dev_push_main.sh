#!/bin/bash

. scripts/env.sh

current_directory=$( pwd );
current_branch=$(git branch --show-current)

# ===== VALIDATION =====

if ! [ "$current_branch" == "dev" ]; then
    printf "${YELLOW}The current branch must be dev${NO_COLOR}\n"
    printf "${LIGHT_RED}Failed${NO_COLOR}\n"
    return
fi

if ! [[ "$current_directory" == *$BASE_DIR ]]; then
    printf "${YELLOW}The current directory must be $BASE_DIR${NO_COLOR}\n"
    printf "${LIGHT_RED}Failed${NO_COLOR}\n"
    return
fi

# ===== PROCESS =====

git checkout main
git merge dev
git push origin main
git checkout dev

printf "${LIGHT_GREEN}Succeed${NO_COLOR}\n"