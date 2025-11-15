/*
define HTTP routes, connect each route to a controller function,
group everything under one Router object
*/
import express from "express";

// import controller functions (logic for each route)
import { redirectToSpotify, handleSpotifyCallback, getTopArtists } from "../controllers/spotifyController.js";

// create router object
const router = express.Router();

// Redirect user to Spotify login
router.get("/login", redirectToSpotify);

// Spotify redirects back to MediaMates/handle spotify callback
router.get("/callback", handleSpotifyCallback);

// Test endpoint - fetch user's top artists; use access tokens to fetch top artists
router.get("/top-artists", getTopArtists);

export default router;
