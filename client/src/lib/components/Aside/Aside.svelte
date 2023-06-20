<script lang="ts">
	import { clickOutside } from '$lib/action/click_outside';
	import AccountIcon from '~icons/mdi/account';
	import MenuIcon from '~icons/mdi/menu';
	import MenuOpenIcon from '~icons/mdi/menu-open';
	import Link from './Link.svelte';

	let sidebarIsOpen = false;

	function changeSidebarStatus() {
		sidebarIsOpen = !sidebarIsOpen;
	}
</script>

<div use:clickOutside on:clickOutside={() => (sidebarIsOpen = false)}>
	<button
		on:click={changeSidebarStatus}
		aria-controls="logo-sidebar"
		type="button"
		class="z-50 fixed text-2xl inline-flex items-center p-1 mt-2 ml-3 text-black rounded-lg sm:hidden hover:bg-red-500 focus:outline-none focus:ring-2 focus:ring-red-400"
	>
		<span class="sr-only">Open sidebar</span>

		{#if sidebarIsOpen}
			<MenuOpenIcon />
		{:else}
			<MenuIcon />
		{/if}
	</button>

	<aside
		id="logo-sidebar"
		class:-translate-x-full={!sidebarIsOpen}
		class="fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0"
		aria-label="Sidebar"
	>
		<div class="h-full px-3 py-12 sm:py-4 overflow-y-auto bg-slate-100">
			<a href="/" class="flex items-center pl-2.5 mb-5">
				<span class="self-center text-xl font-semibold whitespace-nowrap text-black">Exercise</span>
			</a>
			<ul class="space-y-2 font-medium">
				<Link href="/">
					<AccountIcon class="w-6 h-6 text-red-500 transition duration-75 group-hover:text-black" />
					<span class="ml-3">My Data</span>
				</Link>
			</ul>
		</div>
	</aside>
</div>
