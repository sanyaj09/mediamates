import axios from "axios";
import querystring from "querystring";

const CLIENT_ID = process.env.SPOTIFY_CLIENT_ID;
const CLIENT_SECRET = process.env.SPOTIFY_CLIENT_SECRET;
const REDIRECT_URI = process.env.SPOTIFY_REDIRECT_URI;

// Step 1: Build Spotify auth URL
export const getAuthURL = () => {
  const scope = "user-top-read";

  const params = querystring.stringify({
    response_type: "code",
    client_id: CLIENT_ID,
    scope: scope,
    redirect_uri: REDIRECT_URI,
  });

  return `https://accounts.spotify.com/authorize?${params}`;
};

// Step 2: Exchange code for tokens
export const exchangeCodeForToken = async (code) => {
  const tokenURL = "https://accounts.spotify.com/api/token";

  const data = {
    grant_type: "authorization_code",
    code,
    redirect_uri: REDIRECT_URI,
    client_id: CLIENT_ID,
    client_secret: CLIENT_SECRET,
  };

  const response = await axios.post(tokenURL, querystring.stringify(data), {
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
  });

  return response.data; // access_token, refresh_token, expires_in
};

// Step 3: Fetch top artists
export const fetchTopArtists = async (accessToken) => {
  const response = await axios.get(
    "https://api.spotify.com/v1/me/top/artists?limit=10",
    {
      headers: {
        Authorization: `Bearer ${accessToken}`,
      },
    }
  );

  return response.data;
};
