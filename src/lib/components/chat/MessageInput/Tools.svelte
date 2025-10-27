<script lang="ts">
  import { DropdownMenu } from "bits-ui";
  import { onMount, getContext } from "svelte";
  const i18n = getContext("i18n");

  let show = false;
  let button:HTMLElement;
  let buttonWidth:number;
  let resizeObserver: ResizeObserver;

  export let videosize = "720*1280";

  onMount(() => {
    resizeObserver = new ResizeObserver((entries) => {
      buttonWidth = entries[0].contentRect.width;
    });
    if (button) {
      resizeObserver.observe(button);
    }
    return () => {
      if (resizeObserver) resizeObserver.disconnect();
    };
  });

</script>

<DropdownMenu.Root bind:open={show}>
  <DropdownMenu.Trigger>
    <div class="flex flex-row">
      <button bind:this={button} class="flex flex-row items-center primaryButton rounded-full px-4 py-1.5"
        on:click={(e) => {
          e.preventDefault();
        }}>
        <span class="text-xs text-white ml-1 py-0.5">{ videosize }</span>
      </button>
    </div>
  </DropdownMenu.Trigger>
  <DropdownMenu.Content side="right">
    <slot>
      <div class="flex flex-col bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 
        dark:text-gray-300 text-gray-700 shadow-lg px-3 py-5 rounded-2xl mb-14"
        style="margin-left:-{Math.trunc(buttonWidth + 35)}px;">
        <button
          aria-label="model-item"
          class="flex item-center w-full text-left font-medium line-clamp-1 select-none items-center rounded-button p-2 
            hover:bg-gray-100 dark:hover:bg-gray-850 rounded-xl cursor-pointer data-[highlighted]:bg-muted"
          on:click={(e) => {
            e.preventDefault();
            videosize = "480*832";
            show = false;
          }}
        >
          <div class="flex flex-row items-center gap-2 mr-1">
            <svg xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 1024 1024" 
              class="w-[1rem] h-[1rem]"
              fill="currentColor">
              <path d="M689.5366769 68.15830653l-355.0733538 0a88.76833845 88.76833845 0 0 0-88.76833845 88.76833845L245.69498465 867.07335502a88.76833845 88.76833845 0 0 0 88.76833845 88.76833845l355.0733538 0a88.76833845 88.76833845 0 0 0 88.76833845-88.76833845l0-710.14671004a88.76833845 88.76833845 0 0 0-88.76833845-88.76833845z m-355.0733538 55.48021199l355.0733538 0a33.28812646 33.28812646 0 0 1 33.28812768 33.28812646L722.82480458 867.07335502a33.28812646 33.28812646 0 0 1-33.28812768 33.28812646l-355.0733538 0A33.28812646 33.28812646 0 0 1 301.17519542 867.07335502l0-710.14671004a33.28812646 33.28812646 0 0 1 33.28812768-33.28812646z"/>
            </svg>
            <span class="text-sm ml-1">480*832</span>
          </div>
        </button>
        <button
          aria-label="model-item"
          class="flex item-center w-full text-left font-medium line-clamp-1 select-none items-center rounded-button p-2 
            hover:bg-gray-100 dark:hover:bg-gray-850 rounded-xl cursor-pointer data-[highlighted]:bg-muted"
          on:click={(e) => {
            e.preventDefault();
            videosize = "832*480";
            show = false;
          }}
        >
          <div class="flex flex-row items-center gap-2 mr-1">
            <svg xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 1024 1024" 
              class="w-[1rem] h-[1rem]"
              fill="currentColor">
              <path d="M832 256a128 128 0 0 1 128 128v256a128 128 0 0 1-128 128H192a128 128 0 0 1-128-128V384a128 128 0 0 1 128-128h640z m0 64H192a64 64 0 0 0-63.552 56.512L128 384v256a64 64 0 0 0 56.512 63.552L192 704h640a64 64 0 0 0 63.552-56.512L896 640V384a64 64 0 0 0-56.512-63.552L832 320z"/>
            </svg>
            <span class="text-sm ml-1">832*480</span>
          </div>
        </button>
        <button
          aria-label="model-item"
          class="flex item-center w-full text-left font-medium line-clamp-1 select-none items-center rounded-button p-2 
            hover:bg-gray-100 dark:hover:bg-gray-850 rounded-xl cursor-pointer data-[highlighted]:bg-muted"
          on:click={(e) => {
            e.preventDefault();
            videosize = "720*1280";
            show = false;
          }}
        >
          <div class="flex flex-row items-center gap-2 mr-1">
            <svg xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 1024 1024" 
              class="w-[1rem] h-[1rem]"
              fill="currentColor">
              <path d="M689.5366769 68.15830653l-355.0733538 0a88.76833845 88.76833845 0 0 0-88.76833845 88.76833845L245.69498465 867.07335502a88.76833845 88.76833845 0 0 0 88.76833845 88.76833845l355.0733538 0a88.76833845 88.76833845 0 0 0 88.76833845-88.76833845l0-710.14671004a88.76833845 88.76833845 0 0 0-88.76833845-88.76833845z m-355.0733538 55.48021199l355.0733538 0a33.28812646 33.28812646 0 0 1 33.28812768 33.28812646L722.82480458 867.07335502a33.28812646 33.28812646 0 0 1-33.28812768 33.28812646l-355.0733538 0A33.28812646 33.28812646 0 0 1 301.17519542 867.07335502l0-710.14671004a33.28812646 33.28812646 0 0 1 33.28812768-33.28812646z"/>
            </svg>
            <span class="text-sm ml-1">720*1280</span>
          </div>
        </button>
        <button
          aria-label="model-item"
          class="flex item-center w-full text-left font-medium line-clamp-1 select-none items-center rounded-button p-2 
            hover:bg-gray-100 dark:hover:bg-gray-850 rounded-xl cursor-pointer data-[highlighted]:bg-muted"
          on:click={(e) => {
            e.preventDefault();
            videosize = "1280*720";
            show = false;
          }}
        >
          <div class="flex flex-row items-center gap-2 mr-1">
            <svg xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 1024 1024" 
              class="w-[1rem] h-[1rem]"
              fill="currentColor">
              <path d="M832 256a128 128 0 0 1 128 128v256a128 128 0 0 1-128 128H192a128 128 0 0 1-128-128V384a128 128 0 0 1 128-128h640z m0 64H192a64 64 0 0 0-63.552 56.512L128 384v256a64 64 0 0 0 56.512 63.552L192 704h640a64 64 0 0 0 63.552-56.512L896 640V384a64 64 0 0 0-56.512-63.552L832 320z"/>
            </svg>
            <span class="text-sm ml-1">1280*720</span>
          </div>
        </button>
        <button
          aria-label="model-item"
          class="flex item-center w-full text-left font-medium line-clamp-1 select-none items-center rounded-button p-2 
            hover:bg-gray-100 dark:hover:bg-gray-850 rounded-xl cursor-pointer data-[highlighted]:bg-muted"
          on:click={(e) => {
            e.preventDefault();
            videosize = "1080*1920";
            show = false;
          }}
        >
          <div class="flex flex-row items-center gap-2 mr-1">
            <svg xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 1024 1024" 
              class="w-[1rem] h-[1rem]"
              fill="currentColor">
              <path d="M689.5366769 68.15830653l-355.0733538 0a88.76833845 88.76833845 0 0 0-88.76833845 88.76833845L245.69498465 867.07335502a88.76833845 88.76833845 0 0 0 88.76833845 88.76833845l355.0733538 0a88.76833845 88.76833845 0 0 0 88.76833845-88.76833845l0-710.14671004a88.76833845 88.76833845 0 0 0-88.76833845-88.76833845z m-355.0733538 55.48021199l355.0733538 0a33.28812646 33.28812646 0 0 1 33.28812768 33.28812646L722.82480458 867.07335502a33.28812646 33.28812646 0 0 1-33.28812768 33.28812646l-355.0733538 0A33.28812646 33.28812646 0 0 1 301.17519542 867.07335502l0-710.14671004a33.28812646 33.28812646 0 0 1 33.28812768-33.28812646z"/>
            </svg>
            <span class="text-sm ml-1">1080*1920</span>
          </div>
        </button>
        <button
          aria-label="model-item"
          class="flex item-center w-full text-left font-medium line-clamp-1 select-none items-center rounded-button p-2 
            hover:bg-gray-100 dark:hover:bg-gray-850 rounded-xl cursor-pointer data-[highlighted]:bg-muted"
          on:click={(e) => {
            e.preventDefault();
            videosize = "1920*1080";
            show = false;
          }}
        >
          <div class="flex flex-row items-center gap-2 mr-1">
            <svg xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 1024 1024" 
              class="w-[1rem] h-[1rem]"
              fill="currentColor">
              <path d="M832 256a128 128 0 0 1 128 128v256a128 128 0 0 1-128 128H192a128 128 0 0 1-128-128V384a128 128 0 0 1 128-128h640z m0 64H192a64 64 0 0 0-63.552 56.512L128 384v256a64 64 0 0 0 56.512 63.552L192 704h640a64 64 0 0 0 63.552-56.512L896 640V384a64 64 0 0 0-56.512-63.552L832 320z"/>
            </svg>
            <span class="text-sm ml-1">1920*1080</span>
          </div>
        </button>
      </div>
    </slot>
  </DropdownMenu.Content>
</DropdownMenu.Root>