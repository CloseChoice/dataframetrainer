import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);

export default defineConfig({
	plugins: [sveltekit()],
	worker: {
		format: 'es'
	},
	server: {
		// Listen on all ip addresses
		host: true,
		// The port on which the website is accessible
   		port: 5173,
		proxy: {
		  '/files': {
			target: 'http://127.0.0.1:8080',
			changeOrigin: true,
			// secure: false,
			// agent: new http.Agent(),
			rewrite: (path) => path.replace(/^\/files/, '')
		  },
		  '/pyodide-indexurl': {
			target: 'https://cdn.jsdelivr.net',
			changeOrigin: true,
			rewrite: (path) => path.replace(/^\/pyodide-indexurl/, '/pyodide/v0.23.4/full/')
		  },
		  '/backend': {
			target: 'http://127.0.0.1:5000',
			changeOrigin: true,
			rewrite: (path) => path.replace(/^\/backend/, '')
		  }
		}
	  }
});
