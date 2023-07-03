import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import { createRequire } from 'node:module';
import nodeBuiltins from 'rollup-plugin-node-builtins';
import { resolve } from 'path';

const require = createRequire(import.meta.url);

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		proxy: {
		  '/files': {
			target: 'http://127.0.0.1:8080',
			changeOrigin: true,
			// secure: false,
			// agent: new http.Agent(),
			rewrite: (path) => path.replace(/^\/files/, '')
		  }
		}
	  },
	//   resolve: {
	// 	alias: {
	// 	  // fs: require.resolve('rollup-plugin-node-builtins'),
	// 	  https: require.resolve('rollup-plugin-node-builtins'),
	// 	  // http: resolve('rollup-plugin-node-builtins'),
	// 	  // util: resolve('rollup-plugin-node-builtins'),
	// 	  // stream: resolve('rollup-plugin-node-builtins'),
	// 	  // buffer: resolve('rollup-plugin-node-builtins'),
	// 	  // process: resolve('rollup-plugin-node-builtins'),
	// 	  // url: resolve('rollup-plugin-node-builtins'),
	// 	  // querystring: resolve('rollup-plugin-node-builtins'),
	// 	},
	//   },
})
