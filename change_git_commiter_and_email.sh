git filter-branch -f --env-filter "GIT_AUTHOR_NAME='kentatogashi'; GIT_AUTHOR_EMAIL='hoge@example.com'; GIT_COMMITTER_NAME='kentatogashi'; GIT_COMMITTER_EMAIL='hoge@example.com';" HEAD
