<script lang="ts">
  import { getContext, onMount } from "svelte";
  import { goto } from "$app/navigation";

  import {
    mobile,
    chats,
    chatsearch,
    chatId,
    showSidebar,
    user,
    initPageFlag,
    theme,
    threesideAccount,
    showPriceView
  } from "$lib/stores";

  import ShareChatModal from "../chat/ShareChatModal.svelte";
  import ModelSelector from "../chat/ModelSelector.svelte";
  import MenuLines from "../icons/MenuLines.svelte";
  import { getChatById } from "$lib/apis/chats";
  import Setting from "$lib/components/layout/Navbar/Setting.svelte"

  import { getLanguages } from "$lib/i18n";
  import Tooltip from "../common/Tooltip.svelte";

  import { watchAccount, getAccount } from "@wagmi/core";
  import { config as wconfig, clearConnector } from "$lib/utils/wallet/bnb/index";
  import { modal } from "$lib/utils/wallet/bnb/index";
  import { printSignIn, walletSignIn } from "$lib/apis/auths/index";
  import { Base64 } from 'js-base64';
  import { ethers } from "ethers";

  import { getChatList } from "$lib/apis/chats";
  import PriceModal from "../price/PriceModal.svelte";

  const i18n = getContext("i18n");

  export let initNewChat: Function;
  export let shareEnabled: boolean = false;

  export let chat;
  export let selectedModels: any;

  export let showModelSelector = true;

  let showShareChatModal = false;
  let showDownloadChatModal = false;

  let isMobile = false;
  let languages = [];

  let search = "";
  $: if (search) {
    chatsearch.set(search);
  } else {
    chatsearch.set("");
  }
  // Helper function to fetch and add chat content to each chat
  const enrichChatsWithContent = async (chatList: any) => {
    const enrichedChats: any = await Promise.all(
      chatList.map(async (chat: any) => {
        const chatDetails = await getChatById(
          localStorage.token,
          chat.id
        ).catch((error) => null); // Handle error or non-existent chat gracefully
        if (chatDetails) {
          chat.chat = chatDetails.chat; // Assuming chatDetails.chat contains the chat content
        }
        return chat;
      })
    );
    chats.set(enrichedChats);
  };

  onMount(async () => {
    const userAgent = navigator.userAgent || navigator.vendor || window.opera;
    // 检查是否为移动端设备
    isMobile = /android|iPad|iPhone|iPod|IEMobile|Opera Mini/i.test(userAgent);
    languages = await getLanguages();
  });

  watchAccount(wconfig, {
    async onChange() {
      try {
        if ($threesideAccount?.address) {
          clearConnector();
          $threesideAccount = {};
          await signIn();
        } else {
          let account = getAccount(wconfig);
          await walletLogin(account?.address);
          $threesideAccount = account;
        }   
      } catch (error) {
        console.log("wallet login error:", error);
      }
    },
  });
  const connect = () => {
    checkModalTheme();
    modal.open();
  }
  const checkModalTheme = () => {
    if ($theme === "system" || $theme === "light") {
      modal.setThemeMode("light");
    } else {
      modal.setThemeMode("dark");
    }
  }

  // Generate a random message
  function generateRandomMessage(length: number) {
    const randomBytes = new Uint8Array(length);
    crypto.getRandomValues(randomBytes);
    return ethers.hexlify(randomBytes);
  }
  const walletLogin = async (address: string) => {
    const randomMessage = generateRandomMessage(32);
    let combinedText = '';
    for (let i = 0; i < randomMessage.length; i++) {
      let charCode = randomMessage.charCodeAt(i);
      let vectorCharCode = address.charCodeAt(i % address.length);
      combinedText += String.fromCharCode((charCode + vectorCharCode) % 256);
    }
    const signature = Base64.encode(combinedText);
    const walletSignInResult = await walletSignIn({
      address, 
      nonce: randomMessage, 
      address_type: "threeSide", 
      device_id: localStorage.visitor_id || "", 
      signature, 
      id: localStorage.visitor_id || ""
    });
    if (walletSignInResult?.token) {
      localStorage.removeItem("token");
      localStorage.token = walletSignInResult.token;
      user.set(walletSignInResult);
      await chats.set([]); 
      await chats.set(await getChatList(localStorage.token));
    }
  }

  // visit login
  async function signIn() {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    localStorage.removeItem("walletImported");
    localStorage.removeItem("walletKey");
    const res = await printSignIn("");
    localStorage.token = res.token;
    user.set(res);
    getChatList(localStorage.token).then(chatList => {
			chats.set(chatList);
		});
  }

</script>

<ShareChatModal bind:show={showShareChatModal} chatId={$chatId} />
<PriceModal bind:show={$showPriceView}/>
<nav id="nav" class=" sticky md:pt-[30px] pt-2.5 pb-2.5 top-0 flex flex-row justify-center z-30">
  <div class="flex {$mobile ? 'flex-col' : 'flex-row'} max-w-full w-full mx-auto px-5 pt-0.5 md:px-[1rem]">
    {#if $mobile}
      <div class="flex pt-1 pb-3">
        <a
          id="sidebar-new-chat-button"
          class="flex justify-between rounded-xl py-2 transition min-w-[133px]"
          href="/creator"
          draggable="false"
          on:click={async () => {
            await goto("/creator");
            const newChatButton = document.getElementById("new-chat-button");
            setTimeout(() => {
              newChatButton?.click();
              if ($mobile) {
                showSidebar.set(false);
              }
            }, 0);
          }}
        >
          <div class="self-center mx-1.5">
            <img
              src="/creator/static/favicon2.png"
              class="h-[20px]"
              alt="logo"
            />
          </div>
        </a>
        <div class="flex-1 min-w-[20px]"></div>
        <div class="flex items-center {$threesideAccount?.address ? 'bg-gray-100 dark:bg-gray-850 rounded-full p-1' : ''}">
          {#if $threesideAccount?.address}
            <div class="px-2 flex justify-center space-x-2 rounded-full bg-gray-50 dark:bg-gray-800">
              <div class="flex rounded-xl" id="chat-search">
                <div class="self-center pl-1 py-1 rounded-l-xl bg-transparent">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                    class="w-4 h-4"
                  >
                    <path
                      fill-rule="evenodd"
                      d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z"
                      clip-rule="evenodd"
                    />
                  </svg>
                </div>

                <input
                  class="w-full min-w-0 rounded-r-xl py-1 pl-2 pr-4 text-sm bg-transparent dark:text-gray-300 outline-none"
                  placeholder={$i18n.t("Search")}
                  bind:value={search}
                  on:focus={() => {
                  enrichChatsWithContent($chats);
                }}/>
              </div>
            </div>
          
            <Setting />
          {:else}
            <button
              id="connect-wallet-btn"
              class="relative primaryButton flex rounded-lg transition text-white text-sm whitespace-nowrap pl-3 pr-2 py-1 ml-2"
              aria-label="User Menu"
              on:click={(e) => {
                connect();
              }}
            >
              {$i18n.t("Connect Wallet")}
            </button>
          {/if}

          <div class=" self-center size-2">
            <!-- <div class="size-9 object-cover rounded-full bg-primary">
              <img
                src={$user.profile_image_url == ""
                  ? generateInitialsImage($user.name) : $user.profile_image_url}
                  alt="profile"
                  class=" rounded-full size-9 object-cover"/>
            </div> -->
          </div>
        </div>
      </div>
    {/if}
    {#if !$mobile}
      <div
        class="{$showSidebar
          ? 'md:hidden'
          : ''} self-start flex flex-none items-center text-gray-600 dark:text-gray-400 mr-2"
        >
        <button
          id="sidebar-toggle-button"
          class="cursor-pointer p-2.5 flex rounded-xl hover:bg-[#9903E6] hover:text-white transition"
          on:click={() => {
            showSidebar.set(!$showSidebar);
          }}>
          <div class=" m-auto self-center">
            <MenuLines />
          </div>
        </button>
      </div>
    {/if}
    <div class="flex items-center w-full max-w-full">
      <div class="flex items-center">
        <div
          class="overflow-hidden bg-gray-100 dark:bg-gray-850 rounded-full p-2 min-w-[100px]"
        >
          {#if showModelSelector}
            <ModelSelector bind:selectedModels />
          {/if}
        </div>
        <div class="ml-1">
          <button
            id="new-chat-button"
            class=" flex cursor-pointer p-2 rounded-xl hover:bg-[#9903E6] hover:text-white transition"
            on:click={() => {
              $showPriceView = true;
            }}
          >
            <div class=" m-auto self-center">
              <svg xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 1024 1024" 
                version="1.1"
                fill="currentColor"
                class="size-5">
                <path d="M512 1024A512 512 0 1 1 512 0a512 512 0 0 1 0 1024z m0-83.2A428.8 428.8 0 1 0 512 83.2a428.8 428.8 0 0 0 0 857.6z m183.424-681.664c18.176 11.84 20.992 37.12 5.888 56.704l-120.32 154.752h51.456c26.88 0 48.448 16.64 48.448 37.248a33.536 33.536 0 0 1-14.08 26.624 56.576 56.576 0 0 1-34.368 10.88H548.48v31.04h83.968c26.88 0 48.448 16.96 48.448 37.568 0 10.24-5.312 19.648-14.08 26.624a57.28 57.28 0 0 1-34.368 10.88H548.48v70.912c0 26.688-18.432 48.32-41.408 48.32a37.952 37.952 0 0 1-29.12-14.08 52.928 52.928 0 0 1-12.224-34.24v-71.04h-77.44c-26.752 0-48.448-16.96-48.448-37.44 0-10.368 5.44-19.776 14.208-26.624a57.472 57.472 0 0 1 34.304-10.944h77.376v-31.104h-77.44c-26.752 0-48.448-16.64-48.448-37.44 0-10.304 5.44-19.52 14.208-26.368a56.32 56.32 0 0 1 34.304-10.88h54.848l-120.32-154.752c-15.168-19.52-12.608-44.864 5.888-56.64a38.72 38.72 0 0 1 21.12-5.952c14.208 0 29.184 6.848 39.04 19.712L512 431.104l123.072-158.208a49.92 49.92 0 0 1 39.04-19.712c7.552 0 15.04 1.92 21.248 5.952z"/>
              </svg>
            </div>
          </button>
        </div>
      </div>

      <div class="flex-1" />

      <div
        class="self-start flex items-center text-gray-600 dark:text-gray-400"
      >
        <!-- {#if shareEnabled}
          <Menu
            {chat}
            {shareEnabled}
            shareHandler={() => {
              showShareChatModal = !showShareChatModal;
            }}
            downloadHandler={() => {
              showDownloadChatModal = !showDownloadChatModal;
            }}
          >
            <button
              class="hidden md:flex cursor-pointer px-2 py-2 rounded-xl hover:bg-gray-100 dark:hover:bg-gray-850 transition"
              id="chat-context-menu-button"
            >
              <div class=" m-auto self-center">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="size-5"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M6.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM12.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0ZM18.75 12a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z"
                  />
                </svg>
              </div>
            </button>
          </Menu>
        {/if} -->

        <Tooltip content={$i18n.t("New Chat")}>
          <button
            id="new-chat-button"
            class=" flex cursor-pointer p-2 rounded-xl hover:bg-[#9903E6] hover:text-white transition mx-1"
            on:click={() => {
              initNewChat();
            }}
          >
            <div class=" m-auto self-center">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                class="size-6"
              >
                <path
                  d="M5.433 13.917l1.262-3.155A4 4 0 017.58 9.42l6.92-6.918a2.121 2.121 0 013 3l-6.92 6.918c-.383.383-.84.685-1.343.886l-3.154 1.262a.5.5 0 01-.65-.65z"
                />
                <path
                  d="M3.5 5.75c0-.69.56-1.25 1.25-1.25H10A.75.75 0 0010 3H4.75A2.75 2.75 0 002 5.75v9.5A2.75 2.75 0 004.75 18h9.5A2.75 2.75 0 0017 15.25V10a.75.75 0 00-1.5 0v5.25c0 .69-.56 1.25-1.25 1.25h-9.5c-.69 0-1.25-.56-1.25-1.25v-9.5z"
                />
              </svg>
            </div>
          </button>
        </Tooltip>

        {#if $mobile}
          <div
            class="{$showSidebar
              ? 'md:hidden'
              : ''} self-start flex flex-none items-center text-gray-600 dark:text-gray-400"
          >
            <button
              id="sidebar-toggle-button"
              class="cursor-pointer px-2 py-2 flex rounded-xl hover:bg-[#9903E6] hover:text-white transition"
              on:click={() => {
                showSidebar.set(!$showSidebar);
              }}
            >
              <div class=" m-auto self-center">
                <MenuLines />
              </div>
            </button>
          </div>
        {/if}

        {#if !$mobile}
          {#if $initPageFlag}
            <div
              class="flex items-center {$threesideAccount?.address ? 'bg-gray-100 dark:bg-gray-850 rounded-full p-1 md:mr-[30px]' : ''}"
            >
              {#if $threesideAccount?.address}
                <div
                  class="px-2 flex justify-center space-x-2 rounded-full bg-gray-50 dark:bg-gray-800"
                >
                  <div class="flex rounded-xl" id="chat-search">
                    <div
                      class="self-center pl-1 py-2.5 rounded-l-xl bg-transparent"
                    >
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 20 20"
                        fill="currentColor"
                        class="w-4 h-4"
                      >
                        <path
                          fill-rule="evenodd"
                          d="M9 3.5a5.5 5.5 0 100 11 5.5 5.5 0 000-11zM2 9a7 7 0 1112.452 4.391l3.328 3.329a.75.75 0 11-1.06 1.06l-3.329-3.328A7 7 0 012 9z"
                          clip-rule="evenodd"
                        />
                      </svg>
                    </div>

                    <input
                      class="w-full min-w-0 min-w-[60px] rounded-r-xl py-1.5 pl-2 pr-4 text-sm bg-transparent dark:text-gray-300 outline-none"
                      placeholder={$i18n.t("Search")}
                      bind:value={search}
                      on:focus={() => {
                        enrichChatsWithContent($chats);
                      }}
                    />
                  </div>
                </div>
                <Setting />
              {:else}
                <button
                  id="connect-wallet-btn"
                  class="relative primaryButton flex rounded-lg transition text-white text-sm whitespace-nowrap pl-3 pr-2 py-1 ml-2"
                  aria-label="User Menu"
                  on:click={(e) => {
                    connect();
                  }}
                >
                  {$i18n.t("Connect Wallet")}
                </button>
              {/if}

              <div class=" self-center size-2">
                <!-- <div class="size-9 object-cover rounded-full bg-primary">
                  <img
                    src={$user.profile_image_url == ""
                      ? generateInitialsImage($user.name)
                      : $user.profile_image_url}
                    alt="profile"
                    class=" rounded-full size-9 object-cover"/>
                </div> -->
              </div>
            </div>
          {/if}
        {/if}
      </div>
    </div>
  </div>
</nav>
