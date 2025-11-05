<script>
  import { onMount } from 'svelte';
	import { WEBUI_API_BASE_URL } from '$lib/constants';

  // 初始化 Coinbase Wallet SDK
  onMount(() => {
    
  });

  // 发起支付
  async function startPayment() {
    try {
      // 2. 定义 x402 支付参数（符合协议规范）
      const paymentParams = {
        amount: "0.001", // 支付金额
        currency: "USDT", // 支付货币
        destination: "0x8b0b8c7f984dd3f2b580149ade3cdab504d3af1f", // 收款地址
        metadata: { order_id: "ORD-123123123123123123", description: "测试商品支付" }
      };

      // 3. 生成 x402 协议头（用于后端验证）
      const x402Header = `amount=${paymentParams.amount}; currency=${paymentParams.currency}; destination=${paymentParams.destination}`;

      // 4. 调用后端创建支付订单
      const createResponse = await fetch(`${WEBUI_API_BASE_URL}/x402/create-payment`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'CB-402': x402Header
        },
        body: JSON.stringify(paymentParams.metadata)
      });

      const { transaction_id, payment_url, error } = await createResponse.json();
      if (error) throw new Error(error);

      // 5. 唤起 Coinbase Wallet 完成支付
			console.log("============================", payment_url);
      window.open(payment_url, '_blank');

      // 6. 轮询查询支付状态
      const checkInterval = setInterval(async () => {
        const statusResponse = await fetch(`${WEBUI_API_BASE_URL}/check-payment?tx_id=${transaction_id}`);
        const { status } = await statusResponse.json();
        
        if (status === 'completed') {
          console.log("===============支付成功===================");
          clearInterval(checkInterval);
        } else if (status === 'failed') {
					console.log("===============支付失败===================");
          clearInterval(checkInterval);
        }
      }, 3000);

    } catch (err) {
      console.log("===============支付异常===================", err);
      console.error(err);
    }
  }
</script>

<div class="flex flex-col justify-start p-2">
  <h2>x402 支付演示（Svelte + Python）</h2>
  <button class="primaryButton p-2 rounded-lg mt-2 w-[200px]" on:click={startPayment}>发起 0.001 USDT 支付</button>
</div>