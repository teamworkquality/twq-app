#!/bin/bash
npm cache clean
rm -rf node_modules
npm i -@ npm@latest
npm i
npm rb
npm run dev