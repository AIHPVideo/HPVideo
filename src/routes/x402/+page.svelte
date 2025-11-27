<script lang="ts">
  import { onMount, tick } from "svelte";
  import { page } from "$app/stores";
  import { getX402DeOpenAIChatResult } from "$lib/apis/de";
  import { createOpenAITextStream } from "$lib/apis/streaming";
  import VideoLoading from "$lib/components/chat/Messages/VideoLoading.svelte";
  import VideoPlay from "$lib/components/chat/Messages/VideoPlay.svelte";

  let videoLoading = true;
  let videoUrl = "";
  let results: any[] = [];
  const getVideoResult = async (createid: string) => {
    try {
      const [res, controller] = await getX402DeOpenAIChatResult(
        localStorage.token,
        { requestId: createid }
      );

      console.log("=======================", res);

      await tick();

      if (res && res.ok && res.body) {
        const textStream = await createOpenAITextStream(res.body, true);
        for await (const update of textStream) {
          let { value, status, done } = update;
          console.log('=======================', done);
          if (done) {
            results = [...results, { status: "done", content: "over" }];
          } else {
            results = [...results, { status: status, content: value }];
          }
          if (status == "completed") {
            videoLoading = false;
            videoUrl = value;
          }
          await tick();
        }
      }
    } catch (error) {
      results = [...results, { status: "error", content: error }];
    }
  };

  onMount(async () => {
    const queryParams = new URLSearchParams($page.url?.search);
    let createid = queryParams.get("createid");
    await getVideoResult(createid);
  });
</script>

<div class="flex justify-center w-full">
  {#if videoLoading}
    <VideoLoading />
  {:else}
    <VideoPlay bind:videourl={videoUrl} />
  {/if}
</div>
<div>
  {#each results as item}
    <div class="p-1">
      <span class="text-gray-800">{JSON.stringify(item)}</span>
    </div>
  {/each}
</div>
