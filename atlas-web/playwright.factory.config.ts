import {defineConfig} from '@playwright/test';
export default defineConfig({
  testDir:'./e2e/factory-tests',workers:1,fullyParallel:false,timeout:30000,
  use:{baseURL:'http://127.0.0.1:5208',screenshot:'only-on-failure',trace:'retain-on-failure'},
  webServer:[
    {command:'node e2e/factory-start-api.mjs',url:'http://127.0.0.1:5209/api/health',reuseExistingServer:false,timeout:30000},
    {command:'npm run dev -- --host 127.0.0.1 --port 5208 --strictPort',url:'http://127.0.0.1:5208',env:{ATLAS_API_TARGET:'http://127.0.0.1:5209'},reuseExistingServer:false,timeout:30000},
  ],
});
