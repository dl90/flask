let player;
function onYouTubeIframeAPIReady() {
  player = new YT.Player('player', {
    width: '640',
    height: '390',
    videoId: 'NRmSf9VqrUA',
    playerVars: {
      controls: 0,
      loop: 1
    },
    events: {
      'onStateChange': onPlayerStateChange
    }
  })
}

const playerControlButton = document.querySelector('player-control-button')
playerControlButton.onclick = _ => {
  if (player.getPlayerState() === 1) player.pauseVideo()
  else if (player.getPlayerState() === 2) player.playVideo()
}

function onPlayerStateChange (e) {
  const playerPlaySVG = `<svg class='player-control-icon' viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="currentColor" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>`
  const playerPauseSVG = `<svg class='player-control-icon-pause' viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="currentColor" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>`

  while (playerControlButton.firstChild) playerControlButton.removeChild(playerControlButton.firstChild)
  if (player.getPlayerState() === 1) {
    playerControlButton.insertAdjacentHTML( 'afterbegin', playerPauseSVG )
  }
  else if (player.getPlayerState() === 2) {
    playerControlButton.insertAdjacentHTML( 'afterbegin', playerPlaySVG )
  }
}

const addOnclickToPlaybuttons = _ => {
  const playButtonArr = document.querySelectorAll('play-button')
  playButtonArr.forEach( playButton => {
    playButton.onclick = (e) => {
      const currVideoID = player.getVideoUrl().slice(-11)
      const videoID = e.target.parentNode.dataset.videoid
      if (currVideoID === videoID) {
        if (player.getPlayerState() === 1) player.pauseVideo()
        else if (player.getPlayerState() === 2) player.playVideo()
      }
      else {
        if (videoID) player.loadVideoById( videoID )
        else {
          const title = e.target.parentNode.dataset.title
          execute(title, true, e)
        }
      }
    }
  })
}; addOnclickToPlaybuttons()


const loginButton = document.querySelector('.login-button')
loginButton.onclick = _ => authenticate().then(loadClient)


const searchForm = document.querySelector('.search-form')
searchForm.onsubmit = (e) => {
  e.preventDefault()
  const search = e.target.children[0].value
  execute(search, false)
}

function authenticate() {
  return gapi.auth2.getAuthInstance()
    .signIn({ scope: 'https://www.googleapis.com/auth/youtube.force-ssl' })
    .then(
      () => { console.log( 'Sign-in successful'); },
      (err) => { console.error( 'Error signing in', err); }
    )
}

function loadClient() {
  // Add APIKEY below
  gapi.client.setApiKey('APIKEY')
  return gapi.client.load("https://www.googleapis.com/discovery/v1/apis/youtube/v3/rest")
    .then(
      () => { console.log( 'GAPI client loaded for API' ) },
      (err) =>{ console.error( 'Error loading GAPI client for API', err) }
    )
}

// Make sure the client is loaded and sign-in is complete before calling this method.
function execute(search, fromPlaybutton, e) {
  return gapi.client.youtube.search.list({
    'part': 'snippet',
    'maxResults': 1,
    'order': 'relevance',
    'q': `${search} audio`,
    'regionCode': 'ca',
    'relevanceLanguage': 'en',
    'type': 'video',
    'videoCategoryId': '10',
    'videoEmbeddable': 'any',
    'videoSyndicated': 'any'
  }).then(
    (res) => {
      const item = res.result.items[0]
      const videoID = item.id.videoId
      const title = item.snippet.title
      const posterURL = item.snippet.thumbnails.medium.url
      console.log( `YouTube video title: ${title}` )

      if (e) e.target.parentNode.dataset.videoid = videoID

      if (fromPlaybutton) player.loadVideoById( videoID )
      else loadSearchView( search, videoID, posterURL )
    },
    (err) => {
      console.error( 'Execute error', err);
    }
  )
}

gapi.load( 'client:auth2', () => {
  // Add OAuth 2.0 client ID below
  gapi.auth2.init({ client_id: 'CLIENTID' })
    .then( _ => authenticate().then(loadClient) )
})

function loadSearchView ( search, videoID, posterURL ) {
  const template = `
    <album-row-container>
      <h2 class='row-label'>Top result</h2>
      <album-row>
        <album-container data-videoid='${videoID}'><play-button><svg class='play-icon' viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="currentColor" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg></play-button><img class='cover' src='${posterURL}'/></album-container>
      </album-row>
    </album-row-container>
  `
  const albumRowContainerArr = document.querySelectorAll('album-row-container')
  albumRowContainerArr.forEach( a => a.remove() )
  const playlistRowContainerArr = document.querySelectorAll('playlist-row-container')
  playlistRowContainerArr.forEach( a => a.remove() )
  const rowBreakArr = document.querySelectorAll('row-break')
  rowBreakArr.forEach( (a,i) => i > 0 && a.remove() )

  const mainLayout = document.querySelector('main-layout')
  mainLayout.insertAdjacentHTML( 'beforeend', template )
  addOnclickToPlaybuttons()
}
