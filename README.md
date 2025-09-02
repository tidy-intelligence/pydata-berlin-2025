# PyData Berlin 2025

This repo contains the materials for the talk 'Building Reactive Data Apps with Shinylive and WebAssembly' at [PyData Berlin 2025](https://cfp.pydata.org/berlin2025/talk/GPZPFP/).

- Follow me on [LinkedIn](https://www.linkedin.com/in/christophscheuch/)
- Link to [example app](https://tidy-intelligence.github.io/pydata-berlin-2025/) deployed via GitHub Pages

## Talk Summary

WebAssembly is reshaping how Python applications can be delivered - allowing fully interactive apps that run directly in the browser, without a traditional backend server. In this talk, I'll demonstrate how to build reactive, data-driven web apps using Shinylive for Python, combining efficient local storage with Parquet and extending functionality with optional FastAPI cloud services. We'll explore the benefits and limitations of this architecture, share practical design patterns, and discuss when browser-based Python is the right choice. Attendees will leave with hands-on techniques for creating modern, lightweight, and highly responsive Python data applications.

## Talk Description

In recent years, WebAssembly (Wasm) has opened new frontiers for delivering Python applications - enabling fully interactive, browser-native experiences without requiring a traditional server backend. This paradigm shift is particularly exciting for data scientists and developers looking to build lightweight, highly responsive data apps that can be deployed as static websites, reducing infrastructure complexity while improving user experience.

In this talk, I will walk through how to use Shinylive for Python, an emerging framework that combines reactive programming principles with the power of WebAssembly, to create rich data applications that run entirely in the browser. We'll cover how Shinylive translates reactive code into client-side interactions, eliminating the need for round-trips to a Python server. I'll also introduce techniques for integrating efficient local storage (via Apache Parquet) and show how optional FastAPI services can be layered on for hybrid architectures when needed.

This talk is intended for data scientists, machine learning engineers, and Python developers who are interested in building modern web applications without becoming full-time JavaScript engineers. Attendees will leave with practical techniques for building and deploying reactive data apps that run entirely in the browser.
