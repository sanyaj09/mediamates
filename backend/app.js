import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import spotifyRoutes from "./routes/spotify.js";

dotenv.config();

const app = express(); // app is our express application
app.use(cors());
app.use(express.json());

// when someone accesses the root URL (/) through an HTTP GET, send back this message:
app.get("/", (req, res) => {
  res.send("MediaMates backend is running!");
});

// Spotify integration routes; all spotify-related api endpoints will live under /auth/spotify
app.use("/auth/spotify", spotifyRoutes);

export default app;
