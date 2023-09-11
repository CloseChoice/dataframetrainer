import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig, searchForWorkspaceRoot } from 'vite';
import { createRequire } from 'node:module';

const require = createRequire(import.meta.url);

export default defineConfig({
	plugins: [sveltekit()],
	worker: {
		format: 'es'
	},
	server: {
		fs:{
			allow: [searchForWorkspaceRoot(process.cwd()),
			'/node_modules',
			'/.svelte-kit']
		},
		// Listen on all ip addresses
		host: true,
		// The port on which the website is accessible
   		port: 5173
	}
});
