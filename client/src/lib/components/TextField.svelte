<script lang="ts">
	import classNames from 'classnames';

	export let type: 'text' | 'number' | 'email' | 'password' = 'text';
	export let name: string;
	export let id = name;
	export let error: string | null = null;
	export let value: string | null = null;
	export let label: string | null = null;
	export let placeholder: string | undefined = undefined;
	export let required = false;
	export let autocomplete: 'true' | 'false' | undefined = undefined;
	export { customClassNames as class };

	let customClassNames = '';

	let className = classNames(
		customClassNames,
		'bg-white border border-red-300 text-black text-sm rounded-lg focus:ring-red-500 focus:border-red-500 block w-full p-2.5 placeholder-gray-400 focus:ring-red-500 focus:border-red-500'
	);

	let viewPassword: boolean;
	function changeInputView() {
		viewPassword = !viewPassword;
	}

	const handleInput = (event: Event): void => {
		const target = event.target as HTMLInputElement;
		value = target.value;
	};
</script>

{#if label}
	<label for={id} class="block mb-2 font-medium text-black">{label}</label>
{/if}

<input
	{name}
	{id}
	{placeholder}
	{required}
	{autocomplete}
	{type}
	{value}
	class:bg-black={error}
	class:border-red-500={error}
	class:text-red-900={error}
	class:placeholder-red-500={error}
	class:focus:ring-red-500={error}
	class:focus:border-red-500={error}
	class={className}
	on:change
	on:blur
	on:focus
	on:input={handleInput}
/>

{#if error}
	<p class="mt-0.5 text-sm text-red-500 fixed">
		{error}
	</p>
{/if}
