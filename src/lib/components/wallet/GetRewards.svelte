<script lang="ts">
  import { getContext } from "svelte";
  import { getModels as _getModels } from "$lib/utils";

  import {
    mobile,
    settings,
    models
  } from "$lib/stores";

  const i18n = getContext("i18n");

  let modObj:any = [];
  $: {
    let selmodels = $settings?.models ?? ['wan-2.5'];
    if (selmodels.length > 0) {
      modObj = $models.filter(item => selmodels.includes(item?.model));
    }
    if (modObj.length == 0) {
      modObj = [$models.find(item => item?.model === 'wan-2.5')];
    }
  }
</script>

<div>
  <!-- 模型介绍 -->
  {#if modObj}
    <div class="flex flex-col items-center w-full {$mobile ? 'mb-10':'mb-16'}">
      <img class="size-8" src="{modObj[0]?.modelicon}" alt=""/>
      <span class="text-xl font-bold mt-1">{ modObj[0]?.name }</span>
      <span class="w-full max-w-[600px] text-lg text-center mt-2">{ $i18n.t(modObj[0]?.desc) }</span>
    </div>
  {/if}
</div>

<style>
</style>
