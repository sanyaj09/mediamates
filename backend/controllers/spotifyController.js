import { getAuthURL, exchangeCodeForToken, fetchTopArtists } from "../services/spotifyService.js";

// Controller 1- redirects to spotify login page
export const redirectToSpotify = (req, res) => {
  // when the user hits GET /auth/spotify/login, runs redirectToSpotify() to send them to Spotify login screen
  const authURL = getAuthURL();
  return res.redirect(authURL);
};

// controller 2- handles callback after user logs into spotify
export const handleSpotifyCallback = async (req, res) => {
  const code = req.query.code;

  try {
    const tokens = await exchangeCodeForToken(code);

    // temporarily have it return tokens, will need to be updated to store them in a db
    return res.json({
      message: "Spotify connected!",
      tokens
    });

  } catch (error) {
    console.error("Spotify callback error:", error);
    return res.status(500).json({ error: "OAuth failed" });
  }
};

// controller 3- fetch user's top artists
export const getTopArtists = async (req, res) => {
  try {
    const { access_token } = req.query;  // for now, pass token manually

    const artists = await fetchTopArtists(access_token);

    return res.json(artists);

  } catch (err) {
    console.error("Top artists error:", err);
    return res.status(500).json({ error: "Failed fetching top artists" });
  }
};
