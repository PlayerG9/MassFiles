# Search for plugins
### Search for commtits
`https://api.github.com/repos/:owner/:repo/commits`
`https://api.github.com/repos/PlayerG9/MassFiles/commits`
### List (root)files
`https://api.github.com/repos/:owner/:repo/git/trees/:sha`
`https://api.github.com/repos/PlayerG9/MassFiles/git/trees/:sha`
### search for "plugins"
### List plugins
`https://api.github.com/repos/:owner/:repo/git/trees/:sha`
`https://api.github.com/repos/PlayerG9/MassFiles/git/trees/:sha`
### recursive download from plugins
(urls are provided in the json-response)


---

#### `https://api.github.com/repos/PlayerG9/MassFiles/commits`
```json
[
  {
    "sha": "6e5197ca141633e3fcbdbc0b53b35ddb9aa85847",
    "node_id": "MDY6Q29tbWl0Mzc0OTMzODk3OjZlNTE5N2NhMTQxNjMzZTNmY2JkYmMwYjUzYjM1ZGRiOWFhODU4NDc=",
    "commit": {
      "author": {
        "name": "PlayerG9",
        "email": "g9yout@gmail.com",
        "date": "2021-07-05T14:38:04Z"
      },
      "committer": {
        "name": "PlayerG9",
        "email": "g9yout@gmail.com",
        "date": "2021-07-05T14:38:04Z"
      },
      "message": "progress for the app-base\n\n- updated build.py script\n- added hooks for pyinstaller\n- expanded docs\n- improved base\n- added files for comming scripts\n- first test-plugin (markdown)",
      "tree": {
        "sha": "dcd040ed87ff89838aa6e51c1dcf848f1992411c",
        "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/trees/dcd040ed87ff89838aa6e51c1dcf848f1992411c"
      },
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/commits/6e5197ca141633e3fcbdbc0b53b35ddb9aa85847",
      "comment_count": 0,
      "verification": {
        "verified": false,
        "reason": "unsigned",
        "signature": null,
        "payload": null
      }
    },
    "url": "https://api.github.com/repos/PlayerG9/MassFiles/commits/6e5197ca141633e3fcbdbc0b53b35ddb9aa85847",
    "html_url": "https://github.com/PlayerG9/MassFiles/commit/6e5197ca141633e3fcbdbc0b53b35ddb9aa85847",
    "comments_url": "https://api.github.com/repos/PlayerG9/MassFiles/commits/6e5197ca141633e3fcbdbc0b53b35ddb9aa85847/comments",
    "author": {
      "login": "PlayerG9",
      "id": 68517540,
      "node_id": "MDQ6VXNlcjY4NTE3NTQw",
      "avatar_url": "https://avatars.githubusercontent.com/u/68517540?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/PlayerG9",
      "html_url": "https://github.com/PlayerG9",
      "followers_url": "https://api.github.com/users/PlayerG9/followers",
      "following_url": "https://api.github.com/users/PlayerG9/following{/other_user}",
      "gists_url": "https://api.github.com/users/PlayerG9/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/PlayerG9/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/PlayerG9/subscriptions",
      "organizations_url": "https://api.github.com/users/PlayerG9/orgs",
      "repos_url": "https://api.github.com/users/PlayerG9/repos",
      "events_url": "https://api.github.com/users/PlayerG9/events{/privacy}",
      "received_events_url": "https://api.github.com/users/PlayerG9/received_events",
      "type": "User",
      "site_admin": false
    },
    "committer": {
      "login": "PlayerG9",
      "id": 68517540,
      "node_id": "MDQ6VXNlcjY4NTE3NTQw",
      "avatar_url": "https://avatars.githubusercontent.com/u/68517540?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/PlayerG9",
      "html_url": "https://github.com/PlayerG9",
      "followers_url": "https://api.github.com/users/PlayerG9/followers",
      "following_url": "https://api.github.com/users/PlayerG9/following{/other_user}",
      "gists_url": "https://api.github.com/users/PlayerG9/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/PlayerG9/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/PlayerG9/subscriptions",
      "organizations_url": "https://api.github.com/users/PlayerG9/orgs",
      "repos_url": "https://api.github.com/users/PlayerG9/repos",
      "events_url": "https://api.github.com/users/PlayerG9/events{/privacy}",
      "received_events_url": "https://api.github.com/users/PlayerG9/received_events",
      "type": "User",
      "site_admin": false
    },
    "parents": [
      {
        "sha": "e6ef9aefe8edd533aaa6fea2e99ce9624dc7ce9c",
        "url": "https://api.github.com/repos/PlayerG9/MassFiles/commits/e6ef9aefe8edd533aaa6fea2e99ce9624dc7ce9c",
        "html_url": "https://github.com/PlayerG9/MassFiles/commit/e6ef9aefe8edd533aaa6fea2e99ce9624dc7ce9c"
      }
    ]
  },
  ...
]
``` 
=> "sha": "6e5197ca141633e3fcbdbc0b53b35ddb9aa85847" (from first element)
#### `https://api.github.com/repos/PlayerG9/MassFiles/git/trees/:sha`
```json
{
  "sha": "6e5197ca141633e3fcbdbc0b53b35ddb9aa85847",
  "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/trees/6e5197ca141633e3fcbdbc0b53b35ddb9aa85847",
  "tree": [
    {
      "path": ".gitattributes",
      "mode": "100644",
      "type": "blob",
      "sha": "dfe0770424b2a19faf507a501ebfc23be8f54e7b",
      "size": 66,
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/blobs/dfe0770424b2a19faf507a501ebfc23be8f54e7b"
    },
    {
      "path": ".github",
      "mode": "040000",
      "type": "tree",
      "sha": "e1c235f67f6cddb8f83634dff3a15c61f480305b",
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/trees/e1c235f67f6cddb8f83634dff3a15c61f480305b"
    },
    {
      "path": ".gitignore",
      "mode": "100644",
      "type": "blob",
      "sha": "14121cc9cb0d6f64de813de33e3bc51641d8cad9",
      "size": 1415,
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/blobs/14121cc9cb0d6f64de813de33e3bc51641d8cad9"
    },
    {
      "path": "LICENSE",
      "mode": "100644",
      "type": "blob",
      "sha": "e4d3d6040e443d723085ed7d5d35e440bc31959f",
      "size": 1065,
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/blobs/e4d3d6040e443d723085ed7d5d35e440bc31959f"
    },
    {
      "path": "NoteBook",
      "mode": "040000",
      "type": "tree",
      "sha": "961eda0862dc5368f166767eccd60aac3040fdb9",
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/trees/961eda0862dc5368f166767eccd60aac3040fdb9"
    },
    {
      "path": "README.assets",
      "mode": "040000",
      "type": "tree",
      "sha": "df4846565a7a4e36dc007ca95c971035f7162dfd",
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/trees/df4846565a7a4e36dc007ca95c971035f7162dfd"
    },
    {
      "path": "README.md",
      "mode": "100644",
      "type": "blob",
      "sha": "27fe52c05b714fa82afb47945036abf0c56ffda2",
      "size": 640,
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/blobs/27fe52c05b714fa82afb47945036abf0c56ffda2"
    },
    {
      "path": "build",
      "mode": "040000",
      "type": "tree",
      "sha": "32055b31988e2f400afe96aac0acbadc96f09e48",
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/trees/32055b31988e2f400afe96aac0acbadc96f09e48"
    },
    {
      "path": "docs",
      "mode": "040000",
      "type": "tree",
      "sha": "37c0a83e90afa7bc998dbf0dc85e82dd53300a01",
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/trees/37c0a83e90afa7bc998dbf0dc85e82dd53300a01"
    },
    {
      "path": "plugins",
      "mode": "040000",
      "type": "tree",
      "sha": "6d2e3030bf05d9057e8a858c6de850067516abb0",
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/trees/6d2e3030bf05d9057e8a858c6de850067516abb0"
    },
    {
      "path": "requirements.txt",
      "mode": "100644",
      "type": "blob",
      "sha": "b472ba20e0cb18a27590b81fa81fdc0543e2d3b9",
      "size": 50,
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/blobs/b472ba20e0cb18a27590b81fa81fdc0543e2d3b9"
    },
    {
      "path": "runner.py",
      "mode": "100644",
      "type": "blob",
      "sha": "021f61301fe9629a9951351b20a513632245ca15",
      "size": 500,
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/blobs/021f61301fe9629a9951351b20a513632245ca15"
    },
    {
      "path": "temp",
      "mode": "040000",
      "type": "tree",
      "sha": "7a7c113b8b7944a9dcbae83551037eb5e8aa38ca",
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/trees/7a7c113b8b7944a9dcbae83551037eb5e8aa38ca"
    },
    {
      "path": "test.nb",
      "mode": "100644",
      "type": "blob",
      "sha": "3a1519232f0f3c560fbbf57f1d14943271ff0b55",
      "size": 534,
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/blobs/3a1519232f0f3c560fbbf57f1d14943271ff0b55"
    },
    {
      "path": "tests",
      "mode": "040000",
      "type": "tree",
      "sha": "51b7109efd337c9c89a53d7b6a6c8e11a4737004",
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/trees/51b7109efd337c9c89a53d7b6a6c8e11a4737004"
    }
  ],
  "truncated": false
}
```
=> "sha": "6d2e3030bf05d9057e8a858c6de850067516abb0" (from path)
#### `https://api.github.com/repos/PlayerG9/MassFiles/git/trees/:sha`
```json
{
  "sha": "6d2e3030bf05d9057e8a858c6de850067516abb0",
  "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/trees/6d2e3030bf05d9057e8a858c6de850067516abb0",
  "tree": [
    {
      "path": "markdown_plugin",
      "mode": "040000",
      "type": "tree",
      "sha": "27cc6bb2b3634f46e9c643a789642df590c0cac3",
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/trees/27cc6bb2b3634f46e9c643a789642df590c0cac3"
    },
    {
      "path": "test_plugin.py",
      "mode": "100644",
      "type": "blob",
      "sha": "b0ad65853c3ad720f21f136f746aa0560d1a6baf",
      "size": 489,
      "url": "https://api.github.com/repos/PlayerG9/MassFiles/git/blobs/b0ad65853c3ad720f21f136f746aa0560d1a6baf"
    }
  ],
  "truncated": false
}
```
#### recursive download for the files
