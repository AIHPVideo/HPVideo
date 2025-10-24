import { browser, dev } from "$app/environment";
// import { version } from '../../package.json';

export const APP_NAME = "HPVideo";
export const WEBUI_BASE_URL = browser
  ? dev
    ? `http://${location.hostname}:8080`
    : ``
  : ``;

export const WEBUI_API_BASE_URL = `${WEBUI_BASE_URL}/api/v1`;
export const DEGPT_API_BASE_URL = 'https://www.degpt.ai/api/v1';
export const DEGPT_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjQxY2M5ZjhhOWZjMjE2MDNhZWMxNGIxNzBiMGZiNDM0IiwiZXhwIjoxNzY5MDQ0ODE5fQ.fU12478h48wt5Pec6yD5DX4-ALhu1jFAP708Q7qv844';

export const LITELLM_API_BASE_URL = `${WEBUI_BASE_URL}/litellm/api`;
export const OPENAI_API_BASE_URL = `${WEBUI_BASE_URL}/openai/api`;
export const AUDIO_API_BASE_URL = `${WEBUI_BASE_URL}/audio/api/v1`;
export const IMAGES_API_BASE_URL = `${WEBUI_BASE_URL}/images/api/v1`;
export const RAG_API_BASE_URL = `${WEBUI_BASE_URL}/rag/api/v1`;
// export const DE_API_BASE_URL = `https://usa-chat.degpt.ai/api`;
//export const DE_API_BASE_URL = `https://chat.degpt.ai/api`;

export const UPLOAD_API_BASE_URL = `http://localhost:8081/api/v1`;

export const WEBUI_VERSION = APP_VERSION;
export const REQUIRED_OLLAMA_VERSION = "0.1.16";

export const SUPPORTED_FILE_TYPE = [
  "application/epub+zip",
  "application/msword",
  "application/pdf",
  "text/plain",
  "text/csv",
  "text/xml",
  "text/html",
  "text/x-python",
  "text/css",
  "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
  "application/octet-stream",
  "application/x-javascript",
  "text/markdown",
  "audio/mpeg",
  "audio/wav"
];

export const SUPPORTED_FILE_EXTENSIONS = [
  "pdf",
  "ppt",
  "pptx",
  "doc",
  "docx",
  "rtf",
  "xls",
  "xlsx",
  "csv",
  "txt",
  "log",
  "ini",
  "json",
  "md",
  "html",
  "htm",
  "css",
  "ts",
  "js",
  "cpp",
  "asp",
  "aspx",
  "config",
  "sql",
  "plsql",
  "py",
  "go",
  "php",
  "vue",
  "java",
  "c",
  "cs",
  "h",
  "hsc",
  "bash",
  "swift",
  "svelte",
  "env",
  "r",
  "lua",
  "m",
  "mm",
  "perl",
  "rb",
  "rs",
  "db2",
  "scala",
  "dockerfile",
  "yml"
];

// Source: https://kit.svelte.dev/docs/modules#$env-static-public
// This feature, akin to $env/static/private, exclusively incorporates environment variables
// that are prefixed with config.kit.env.publicPrefix (usually set to PUBLIC_).
// Consequently, these variables can be securely exposed to client-side code.

export const DefaultCurrentWalletData = {
  walletInfo: null,
  dbcBalance: "0",
  dgcBalance: "0",
  price: {
    dbc: 0,
    dlc: 0,
  },
};

export const RewardProperties = {
  "regist": "10,000",
  "invite": "10,000",
  "ipeoples": 20,
  "itimes": 3,
  "clockin": "1,000",
  "clockinall": "30,000",
  "civalid": 180,
  "citimes": 30,
  "endtime": "2025-09-17 00:00:00"
}

// 升级VIP钱包地址
// export const tranAddress = "0x75A877EAB8CbD11836E27A137f7d0856ab8b90f8" 测试使用
export const tranAddress = "0x40Ff2BD3668B38B0dd0BD7F26Aa809239Fc9113a"
