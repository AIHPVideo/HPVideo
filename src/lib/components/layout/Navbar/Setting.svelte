<script lang="ts">
  import { getContext } from "svelte";
  import { DropdownMenu } from "bits-ui";
  import { flyAndScale } from "$lib/utils/transitions";
  import { mobile } from "$lib/stores";

  import UserEdit from "$lib/components/chat/Settings/UserEdit.svelte";
  import { toast } from 'svelte-sonner';

  const i18n = getContext("i18n");

  let show = false;

</script>

<DropdownMenu.Root bind:open={show}>
  <DropdownMenu.Trigger>
    <button
      class="relative flex rounded-xl transition pl-3 pr-2 py-2"
      aria-label="User Menu"
      on:click={(e) => {
        e.preventDefault(); 
      }}
    >
      <svg xmlns="http://www.w3.org/2000/svg" 
        class="size-5"
        viewBox="0 0 16 16">
        <path fill="currentColor" d="M7.954 1.372a1 1 0 0 1 1.414-.15l3.262 2.664a1 1 0 0 1 .25 1.245A3 3 0 0 0 12 5h-.3l.298-.34l-1.718-1.403l-1.417 1.744H7.574l1.931-2.376l-.77-.629L6.337 5h-1.28zM10.5 10a.5.5 0 0 0 0 1h1a.5.5 0 0 0 0-1zM3 5.5a.5.5 0 0 1 .5-.5h.558l.795-1H3.5A1.5 1.5 0 0 0 2 5.5v6A2.5 2.5 0 0 0 4.5 14H12a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2H3.5a.5.5 0 0 1-.5-.5m0 6V6.915q.236.084.5.085H12a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H4.5A1.5 1.5 0 0 1 3 11.5"></path>
      </svg>
      <div class="absolute top-0 right-1 w-3 h-3 rounded-full border-2 border-white dark:border-gray-800 bg-[#C213F2] shadow-lg" title="Wallet connected"></div>
    </button>
  </DropdownMenu.Trigger>
  <DropdownMenu.Content
    class="z-[90] {$mobile
      ? `w-full max-w-[90%]`
      : `min-w-[365px] max-w-[80%]`}  justify-start rounded-2xl  bg-white dark:bg-gray-850 dark:text-white shadow-lg 
      border border-gray-300/30 dark:border-gray-700/50  outline-none"
    transition={flyAndScale}
    side="bottom"
    sideOffset={12}
    align="end"
    alignOffset={10}
  >
    <slot>
      <div class="text-gray-700 dark:text-gray-100">
        <div class="flex flex-col md:flex-col w-full px-4 py-2 md:space-x-4">
          <div class="flex-1 md:mt-3 md:min-h-[10rem]">
            <UserEdit
              saveHandler={() => {
                toast.success($i18n.t("Settings saved successfully!"));
                show = false;
              }}
            />
          </div>
        </div>
      </div>
    </slot>
  </DropdownMenu.Content>
</DropdownMenu.Root>
