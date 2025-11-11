import { signMessage } from "@wagmi/core";
import { defaultWagmiConfig } from "@web3modal/wagmi";
import { base } from 'viem/chains'

// 1. Define constants
export const projectId = "59443aa943b8865491317c04a19a8be3";

// 2. Create wagmiConfig
const metadata = {
  name: "hpvideo",
  description: "Web3Modal Example",
  url: "https://web3modal.com",
  icons: ["https://avatars.githubusercontent.com/u/37784886"],
};

const chains: any = [ base ];

export const config = defaultWagmiConfig({
  projectId,
  chains,
  metadata
});

export const walletconnectSignMessage = async (message: string) => {
  try {
    // const message = "This is a demo message.";
    const signature = await signMessage(config, { message });
    return signature;
  } catch (error) {
    return message;
  }
};