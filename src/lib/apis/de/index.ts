import { promptTemplate } from "$lib/utils";
import { WEBUI_API_BASE_URL, DEGPT_API_BASE_URL } from '$lib/constants';

// 获取De的所有模型列表
export const getDeModels = async (token: string = "") => {

  const format_res = {
    models: [
      // 基础模型
      {
        name: "WAN 2.5",
        source: "alibaba",
        model: "wan-2.5",
        textmodel: "text-to-video",
        imagemodel: "image-to-video",
        tip: "WAN 2.5",
        support: "image",
        type: 1,
        desc: "Suitable for reasoning and writing",
        modelicon: "/static/icon/qwen.png",
        modelinfo: ""
      },
      {
        name: "SORA 2",
        source: "openai",
        model: "sora-2.5",
        textmodel: "text-to-video",
        imagemodel: "image-to-video",
        tip: "SORA 2",
        support: "image",
        type: 1,
        desc: "Suitable for reasoning and writing",
        modelicon: "/static/icon/gpt3.png",
        modelinfo: ""
      }
    ],
  };
  return (format_res?.models ?? []).map((model) => ({
    id: model.model,
    name: model.name ?? model.model,
    ...model,
  }));
};

// ai会话请求封装
export const getDeOpenAIChatCompletion = async (
  token: string = "",
  body: Object
) => {
  let res: any;
  let error = null;
  const controller = new AbortController();
  try {
    res = await fetch(`${WEBUI_API_BASE_URL}/chat/completion/video`, {
      signal: controller.signal,
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        ...body,
        project: "HPVideo"
      }),
    });
    if (res.status != 200) {
      throw new Error("error");
    }
  } catch (err) {
    error = err;
    res = null;
  }

  if (error) {
    throw error;
  }

  return [res, controller];
}

// Add a shorthand
export const generateDeTitle = async (
  token: string = "",
  template: string,
  model: string,
  prompt: string
) => {
  let error = null;
  let res: any;
  template = promptTemplate(template, prompt);
  model = 'qwen3-235b-a22b';
  try {
    const result = await fetch(`${DEGPT_API_BASE_URL}/chat/completion/proxy`, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        model: model,
        // node_id: nodeList?.[0],
        messages: [
          {
            role: "user",
            content: template,
          },
        ],
        stream: false,
        project: "DecentralGPT",
        // Restricting the max tokens to 50 to avoid long titles
        max_tokens: 50,
        enable_thinking: false,
        reload: false,
        audio: false
      })
    });
    res = await result.json();
  } catch (err) {
    error = err;
    console.log("Request Error");
  }

  if (error) {
    throw error;
  }

  return (
    res?.choices[0]?.message?.content.replace(/["']/g, "") ?? "New Chat"
  );
};