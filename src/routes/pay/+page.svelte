<script lang="ts">
  import { onMount } from "svelte";
  import { ethers } from "ethers";
  import { theme } from "$lib/stores";
  import { WEBUI_API_BASE_URL } from '$lib/constants';

  import { createWeb3Modal } from "@web3modal/wagmi";
  import { config, projectId } from "$lib/utils/wallet/index";
  import { watchConnections, getAccount } from "@wagmi/core";

  let address: string = "";
  let modal: any = { options: { themeMode: "dark" } };
  onMount(() => {
    const account = getAccount(config);
    if (account?.address) {
      address = account?.address;
    }

    watchConnections(config, {
      async onChange(data) {
        if (address == "") {
          if (data.length) {
            address = data[0].accounts[0];
          } else {
            address = "";
          }
        } else {
          clearConnector();
          address = "";
        }
      },
    });

    modal = createWeb3Modal({
      themeMode: "dark",
      wagmiConfig: config,
      projectId,
      enableAnalytics: true,
      enableOnramp: true,
    });
  });
  function clearConnector() {
    config.state.connections.forEach((item) => {
      config.state.connections.delete(item.connector.uid);
    });
  }

  function checkModalTheme() {
    if ($theme === "system" || $theme === "light") {
      modal.setThemeMode("light");
    } else {
      modal.setThemeMode("dark");
    }
  }

  function connect() {
    checkModalTheme();
    modal.open();
  }

  // format wallet address
  function formatAddress(address: string) {
    return `${address.slice(0, 6)}...${address.slice(-4)}`;
  }

  // start pay
  async function startPayment() {
    if (!checkWalletConnect()) {
      return;
    }
    try {
      const response = await fetch(`${WEBUI_API_BASE_URL}/x402/creator?model=wan2.5&messageid=2222222`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
      });
      if (response.status == 402) {
        const paymentInfo = await response.json();
        // sign to pay
        await handleWeb3Payment(paymentInfo);
      }
    } catch (err) {
      console.error(err);
    }
  }

  // check wallet connect
  function checkWalletConnect() {
    // 检查是否安装 Web3 钱包
    if (typeof window.ethereum === "undefined") {
      throw new Error("Web3 wallet not found. Please install.");
    }
    // 连接钱包
    if (address == "") {
      connect();
      return false;
    } else {
      return true;
    }
  }

  // sign to pay
  async function handleWeb3Payment(paymentInfo: any) {
    try {
      const paymentScheme = paymentInfo.accepts[0];
      const { resource } = paymentScheme;

      const xpayment = await createXPaymentHeader(paymentInfo);

      const response = await fetch(resource, {
        method: "GET",
        headers: {
          "X-PAYMENT": xpayment,
          "Content-Type": "application/json",
        },
      });
      if (response.ok) {
        const data = await response.json();
        console.log("==============支付成功===========", data);
      } else {
        const error = await response.text();
        console.log("==============支付失败===========", error);
      }
    } catch (error) {
      console.error("Web3 payment failed:", error);
      throw error;
    }
  }

  // create Base64 X-PAYMENT header
  async function createXPaymentHeader(paymentInfo: any) {
    // get wallet signer
    const account = getAccount(config);
    const provider: any = await account?.connector?.getProvider();
    const eprovider = new ethers.BrowserProvider(provider);
    await eprovider.send("eth_requestAccounts", []);
    const signer = await eprovider.getSigner();

    const paymentScheme = paymentInfo.accepts[0];
    const { payTo, maxAmountRequired } = paymentScheme;
    const timestamp = Math.floor(Date.now() / 1000);

    const paymentPayload = {
      x402Version: paymentInfo.x402Version,
      scheme: paymentScheme.scheme,
      network: paymentScheme.network,
      payload: {
        signature: "",
        authorization: {
          from: account?.address?.toLowerCase(),
          to: payTo,
          value: maxAmountRequired,
          validAfter: timestamp.toString(),
          validBefore: (timestamp + 600).toString(),
          nonce: ethers.hexlify(ethers.randomBytes(32))
        },
      },
    };

    const msg = JSON.stringify(paymentPayload.payload.authorization);
    const signature = await signer.signMessage(msg);
    paymentPayload.payload.signature = signature;
    const paymentPayloadString = JSON.stringify(paymentPayload);
    const base64EncodedPayload = Buffer.from(paymentPayloadString).toString("base64");
    return base64EncodedPayload;
  }
</script>

<div class="flex flex-col justify-start p-2">
  <h2>x402 支付演示（Svelte + Python）</h2>
  <button class="primaryButton p-2 rounded-lg mt-2 w-[200px]" on:click={connect}
    >{address == "" ? "连接钱包" : formatAddress(address)}</button
  >
  <button
    class="primaryButton p-2 rounded-lg mt-2 w-[200px]"
    on:click={startPayment}>发起 0.001 USDT 支付</button
  >
</div>
