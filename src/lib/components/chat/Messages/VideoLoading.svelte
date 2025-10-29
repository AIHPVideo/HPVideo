<script lang="ts">
	import { getContext } from 'svelte';
	import { mobile } from "$lib/stores";
	const i18n = getContext('i18n');
	export let videosize = '16/9';
	let aspectRatio = '16/9';

	$: if(videosize) {
		if (videosize.includes('*')) {
			if (Number(videosize.split('*')[0]) > Number(videosize.split('*')[1])) {
				aspectRatio = '16/9';
			} else {
				aspectRatio = '9/16';
			}
		} else if (videosize.includes(':')) {
			if (Number(videosize.split(':')[0]) > Number(videosize.split(':')[1])) {
				aspectRatio = '16/9';
			} else {
				aspectRatio = '9/16';
			}
		} else {
			aspectRatio = '16/9';
		}
	}

</script>

<div class="w-full mt-3 mb-4">
	<div class="animate-pulse flex w-full">
		<div class="flex justify-center flex-col items-center w-full {$mobile ? '' : 'max-w-[600px]'} rounded-lg
			bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500" style={`aspect-ratio: ${aspectRatio}`}>
			<img class="size-10" src="/static/video/video_generating.png" alt=""/>
			<span class="text-sm text-gray-50 mt-1">{ $i18n.t("Video Generating...") }</span>
		</div>
	</div>
</div>