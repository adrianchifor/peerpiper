# PeerPiper

Free, fast and simple P2P file transfer using WebTorrent.

The app was created in 24h at TechCrunch Disrupt London Hackathon 2016. For more information check out the [Devpost project page](https://devpost.com/software/peerpiper).

Uses Redis for storing file names and magnet links.

## Env vars
```
REDIS_URL (if using dokku, will be automatically set when linking with Redis service)
```

## Run

Using [dokku](http://dokku.viewdocs.io/dokku/):
* Create `peerpiper` app on dokku
* Create a Redis service on dokku using this [plugin](https://github.com/dokku/dokku-redis) and link it with `peerpiper` (this will set the `REDIS_URL` env var)
* Set the dokku remote in the git repo:
`git remote add dokku dokku@example.com:peerpiper`
* Deploy:
`git push dokku master`

### License

Copyright &copy; 2018 Adrian Chifor, Jose Diez

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
