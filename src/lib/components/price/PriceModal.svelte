<script lang="ts">
	import { getContext } from "svelte";
	import Modal from "../common/Modal.svelte";
	import { models } from "$lib/stores";

	const i18n = getContext("i18n");

	export let show = false;
</script>

<Modal size="lg" bind:show>
	<div class="max-h-[80vh] xs:h-auto flex flex-col">
		<div class=" flex justify-between dark:text-gray-300 px-5 pt-6 pb-2">
			<div class=" text-base font-bold self-center">{$i18n.t("Pricing")}</div>
			<button
				class="self-center"
				on:click={() => {
					show = false;
				}}
			>
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 20 20"
					fill="currentColor"
					class="w-5 h-5"
				>
					<path
						d="M6.28 5.22a.75.75 0 00-1.06 1.06L8.94 10l-3.72 3.72a.75.75 0 101.06 1.06L10 11.06l3.72 3.72a.75.75 0 101.06-1.06L11.06 10l3.72-3.72a.75.75 0 00-1.06-1.06L10 8.94 6.28 5.22z"
					/>
				</svg>
			</button>
		</div>

		<div class="flex flex-col h-1/3 overflow-y-auto pb-6 md:px-8 px-4 mt-4">
			<div class="flex flex-row justify-center items-center border-t border-l border-r border-gray-600 dark:border-gray-100 rounded-t-lg">
				<div class="text-center font-bold text-sm py-2 md:w-[150px] w-[100px] px-1 border-r border-gray-600 dark:border-gray-100">{$i18n.t("Model")}</div>
				<div class="flex-1 text-center font-bold text-sm py-2 border-l border-gray-600 dark:border-gray-100">{$i18n.t("Size")}</div>
				<div class="flex-1 text-center font-bold text-sm py-2 border-l border-gray-600 dark:border-gray-100">{$i18n.t("Duration")}</div>
				<div class="flex-1 text-center font-bold text-sm py-2 border-l border-gray-600 dark:border-gray-100">{$i18n.t("Price")}</div>
			</div>
			{#each $models as item, index}
				<div class="flex flex-row justify-center items-center border-t border-l border-r border-gray-600 dark:border-gray-100
					{(index == $models.length - 1) ? 'border-b rounded-b-lg' : ''}">
					<div class="text-center font-bold text-sm py-2 md:w-[150px] w-[100px] px-1">
						{item.name}
					</div>
					<div class="flex-1 flex flex-col w-full">
						{#each item?.size as sitem, sindex}
							<div
								class="flex flex-row w-full items-center border-b border-l border-gray-600 dark:border-gray-100
								{(sindex == item.size.length - 1) ? 'border-b-0' : ''}"
							>
								<div class="flex-1 flex justify-center">{sitem}</div>
								<div class="flex-1">
									{#each item?.duration as ditem, dindex}
										<div
											class="flex justify-center {dindex ==
											item?.duration.length - 1
												? ''
												: 'border-b'} border-l border-gray-600 dark:border-gray-100 py-1"
										>
											{ditem}s
										</div>
									{/each}
								</div>
								<div class="flex-1">
									{#each Object.entries(item?.amount) as [key, avals]}
										{#if sitem.includes(key) || key == "*"}
											{#each avals as aitem, aindex}
												<div
													class="flex justify-center {aindex == avals.length - 1
														? ''
														: 'border-b'} border-l border-gray-600 dark:border-gray-100 py-1"
												>
													${aitem}
												</div>
											{/each}
										{/if}
									{/each}
								</div>
							</div>
						{/each}
					</div>
				</div>
			{/each}
		</div>
	</div>
</Modal>
