import { APP_NAME, DefaultCurrentWalletData } from '$lib/constants';
import { type Writable, writable } from 'svelte/store';

// Backend
export const WEBUI_NAME = writable(APP_NAME);
export const config: Writable<Config | undefined> = writable(undefined);
export const user: Writable<SessionUser | undefined> = writable(undefined);

// Frontend
export const MODEL_DOWNLOAD_POOL = writable({});

export const mobile = writable(false);

export const theme = writable('light');
// export const theme = writable('dark');
export const chatId = writable('');

export const chats = writable([]);
export const tags = writable([]);
export const models: Writable<Model[]> = writable([]);

export const modelfiles = writable([]);
export const prompts: Writable<Prompt[]> = writable([]);
export const documents = writable([
	{
		collection_name: 'collection_name',
		filename: 'filename',
		name: 'name',
		title: 'title'
	},
	{
		collection_name: 'collection_name1',
		filename: 'filename1',
		name: 'name1',
		title: 'title1'
	}
]);

export const settings: Writable<Settings> = writable({});

export const showSidebar = writable(false);
export const showSettings = writable(false);
export const showArchivedChats = writable(false);
export const showChangelog = writable(false);


// ###########
// 钱包相关
export const showNewWalletModal = writable(false);
export const showOpenWalletModal = writable(false);
export const showExportWalletJsonModal = writable(false);
export const showTransferModal = writable(false);
export const showPriceModal = writable(false);
export const showBuyCoinModal = writable(false);
export const showShareModal = writable(false);
export const showRewardsModal = writable(false);
export const showRewardsHistoryModal = writable(false);
export const showRewardDetailModal = writable(false);
export const showTransactionsModal = writable(false);
export const showUserVerifyModal = writable(false);
export const showConfirmUpgradeModal = writable(false);
export const showCoinIntruModal = writable(false);
export const showCoinIntruType = writable('dgc');
export const dbcRate = writable({rate: 0.0002});
export const dgcRate = writable({rate: 0.00001});

// 升级VIP标志用于实时更新升级数据
export const vipupgrade = writable(false);


// 页面初始化完成状态
export const initPageFlag = writable(false);

// 下载相关
export const showDownLoad = writable(false);
export const downLoadUrl = writable('')

// 用户钱包视图
export const showWalletView = writable(false);

// 人脸认证url
export const faceUrl = writable({url: ""});

// 推特相关
export const showFollowTwitterModal = writable(false);
export const showFollowTGGroupModal = writable(false);

// 钱包数据
export let currentWalletData = writable(DefaultCurrentWalletData)
export let threesideAccount = writable({})

// 模型访问数量
export let modelLimits = writable([
	{name: 'Llama-3.1-405B', num: 10},
	{name: 'Qwen2-72B', num: 10},
	{name: 'Gemma-2-27B', num: 10},
	{name: 'Codestral-22B-v0.1', num: 10}
])

export let pageUpdateNumber = writable(0)


// 邀请人id
export let inviterId = writable("")

// 来源频道
export let channel = writable("")

// 切换模型相关
export const switchModel = writable({
	content: '',
	toolFlag: false,
	toolType: 'web',
	status: false
});

// 本地保存私钥和密码
export const checkPasswordShow = writable(false);
export const checkPasswordShow2 = writable(false);
export const walletKey = writable({
	privateKey: "",
	checked: false,
	password: ""
})

// 判断是否是币安浏览器
export const binanceFlag = writable(false);

// ###########


type Model = OpenAIModel | OllamaModel;

type OpenAIModel = {
	id: string;
	name: string;
	external: boolean;
	source?: string;
};

type OllamaModel = {
	id: string;
	name: string;

	// Ollama specific fields
	details: OllamaModelDetails;
	size: number;
	description: string;
	model: string;
	modified_at: string;
	digest: string;
};

type OllamaModelDetails = {
	parent_model: string;
	format: string;
	family: string;
	families: string[] | null;
	parameter_size: string;
	quantization_level: string;
};

type Settings = {
	models?: string[];
	conversationMode?: boolean;
	speechAutoSend?: boolean;
	responseAutoPlayback?: boolean;
	audio?: AudioSettings;
	showUsername?: boolean;
	saveChatHistory?: boolean;
	notificationEnabled?: boolean;
	title?: TitleSettings;
	splitLargeDeltas?: boolean;
	chatDirection: 'LTR' | 'RTL';

	system?: string;
	requestFormat?: string;
	keepAlive?: string;
	seed?: number;
	temperature?: string;
	repeat_penalty?: string;
	top_k?: string;
	top_p?: string;
	num_ctx?: string;
	options?: ModelOptions;
};

type ModelOptions = {
	stop?: boolean;
};

type AudioSettings = {
	STTEngine?: string;
	TTSEngine?: string;
	speaker?: string;
	model?: string;
};

type TitleSettings = {
	auto?: boolean;
	model?: string;
	modelExternal?: string;
	prompt?: string;
};

type Prompt = {
	command: string;
	user_id: string;
	title: string;
	content: string;
	timestamp: number;
};

type Config = {
	status?: boolean;
	name?: string;
	version?: string;
	default_locale?: string;
	images?: boolean;
	default_models?: string;
	default_prompt_suggestions?: PromptSuggestion[];
	trusted_header_auth?: boolean;
};

type PromptSuggestion = {
	content: string;
	title: [string, string];
};

type SessionUser = {
	id: string;
	email: string;
	name: string;
	role: string;
	profile_image_url: string;
	address_type: string;
	verified: boolean;
	isPro: boolean;
	proEndDate: string;
};
