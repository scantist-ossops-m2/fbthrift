// @generated by Thrift for thrift/compiler/test/fixtures/exceptions/src/module.thrift
// This file is probably not the place you want to edit!

//! Client implementation for each service in `module`.

#![recursion_limit = "100000000"]
#![allow(non_camel_case_types, non_snake_case, non_upper_case_globals, unused_crate_dependencies, unused_imports, clippy::all)]


#[doc(inline)]
pub use :: as types;

pub mod errors;

pub(crate) use crate as client;
pub(crate) use ::::services;


/// Client definitions for `Raiser`.
pub struct RaiserImpl<P, T, S = ::fbthrift::NoopSpawner> {
    transport: T,
    _phantom: ::std::marker::PhantomData<fn() -> (P, S)>,
}

impl<P, T, S> RaiserImpl<P, T, S>
where
    P: ::fbthrift::Protocol,
    T: ::fbthrift::Transport,
    P::Frame: ::fbthrift::Framing<DecBuf = ::fbthrift::FramingDecoded<T>>,
    ::fbthrift::ProtocolEncoded<P>: ::fbthrift::BufMutExt<Final = ::fbthrift::FramingEncodedFinal<T>>,
    P::Deserializer: ::std::marker::Send,
    S: ::fbthrift::help::Spawner,
{
    pub fn new(
        transport: T,
    ) -> Self {
        Self {
            transport,
            _phantom: ::std::marker::PhantomData,
        }
    }

    pub fn transport(&self) -> &T {
        ::fbthrift::help::GetTransport::transport(self)
    }


    fn _doBland_impl(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoBlandError>> {
        use ::tracing::Instrument as _;
        use ::futures::FutureExt as _;

        const SERVICE_NAME: &::std::ffi::CStr = c"Raiser";
        const SERVICE_METHOD_NAME: &::std::ffi::CStr = c"Raiser.doBland";
        let args = self::Args_Raiser_doBland {
            _phantom: ::std::marker::PhantomData,
        };

        let transport = self.transport();

        // need to do call setup outside of async block because T: Transport isn't Send
        let request_env = match ::fbthrift::help::serialize_request_envelope::<P, _>("doBland", &args) {
            ::std::result::Result::Ok(res) => res,
            ::std::result::Result::Err(err) => return ::futures::future::err(err.into()).boxed(),
        };

        let call = transport
            .call(SERVICE_NAME, SERVICE_METHOD_NAME, request_env, rpc_options)
            .instrument(::tracing::trace_span!("call", method = "Raiser.doBland"));

        async move {
            let reply_env = call.await?;

            let de = P::deserializer(reply_env);
            let res = ::fbthrift::help::async_deserialize_response_envelope::<P, crate::errors::raiser::DoBlandReader, S>(de).await?;

            let res = match res {
                ::std::result::Result::Ok(res) => res,
                ::std::result::Result::Err(aexn) => {
                    ::std::result::Result::Err(crate::errors::raiser::DoBlandError::ApplicationException(aexn))
                }
            };
            res
        }
        .instrument(::tracing::info_span!("stream", method = "Raiser.doBland"))
        .boxed()
    }

    fn _doRaise_impl(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoRaiseError>> {
        use ::tracing::Instrument as _;
        use ::futures::FutureExt as _;

        const SERVICE_NAME: &::std::ffi::CStr = c"Raiser";
        const SERVICE_METHOD_NAME: &::std::ffi::CStr = c"Raiser.doRaise";
        let args = self::Args_Raiser_doRaise {
            _phantom: ::std::marker::PhantomData,
        };

        let transport = self.transport();

        // need to do call setup outside of async block because T: Transport isn't Send
        let request_env = match ::fbthrift::help::serialize_request_envelope::<P, _>("doRaise", &args) {
            ::std::result::Result::Ok(res) => res,
            ::std::result::Result::Err(err) => return ::futures::future::err(err.into()).boxed(),
        };

        let call = transport
            .call(SERVICE_NAME, SERVICE_METHOD_NAME, request_env, rpc_options)
            .instrument(::tracing::trace_span!("call", method = "Raiser.doRaise"));

        async move {
            let reply_env = call.await?;

            let de = P::deserializer(reply_env);
            let res = ::fbthrift::help::async_deserialize_response_envelope::<P, crate::errors::raiser::DoRaiseReader, S>(de).await?;

            let res = match res {
                ::std::result::Result::Ok(res) => res,
                ::std::result::Result::Err(aexn) => {
                    ::std::result::Result::Err(crate::errors::raiser::DoRaiseError::ApplicationException(aexn))
                }
            };
            res
        }
        .instrument(::tracing::info_span!("stream", method = "Raiser.doRaise"))
        .boxed()
    }

    fn _get200_impl(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get200Error>> {
        use ::tracing::Instrument as _;
        use ::futures::FutureExt as _;

        const SERVICE_NAME: &::std::ffi::CStr = c"Raiser";
        const SERVICE_METHOD_NAME: &::std::ffi::CStr = c"Raiser.get200";
        let args = self::Args_Raiser_get200 {
            _phantom: ::std::marker::PhantomData,
        };

        let transport = self.transport();

        // need to do call setup outside of async block because T: Transport isn't Send
        let request_env = match ::fbthrift::help::serialize_request_envelope::<P, _>("get200", &args) {
            ::std::result::Result::Ok(res) => res,
            ::std::result::Result::Err(err) => return ::futures::future::err(err.into()).boxed(),
        };

        let call = transport
            .call(SERVICE_NAME, SERVICE_METHOD_NAME, request_env, rpc_options)
            .instrument(::tracing::trace_span!("call", method = "Raiser.get200"));

        async move {
            let reply_env = call.await?;

            let de = P::deserializer(reply_env);
            let res = ::fbthrift::help::async_deserialize_response_envelope::<P, crate::errors::raiser::Get200Reader, S>(de).await?;

            let res = match res {
                ::std::result::Result::Ok(res) => res,
                ::std::result::Result::Err(aexn) => {
                    ::std::result::Result::Err(crate::errors::raiser::Get200Error::ApplicationException(aexn))
                }
            };
            res
        }
        .instrument(::tracing::info_span!("stream", method = "Raiser.get200"))
        .boxed()
    }

    fn _get500_impl(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get500Error>> {
        use ::tracing::Instrument as _;
        use ::futures::FutureExt as _;

        const SERVICE_NAME: &::std::ffi::CStr = c"Raiser";
        const SERVICE_METHOD_NAME: &::std::ffi::CStr = c"Raiser.get500";
        let args = self::Args_Raiser_get500 {
            _phantom: ::std::marker::PhantomData,
        };

        let transport = self.transport();

        // need to do call setup outside of async block because T: Transport isn't Send
        let request_env = match ::fbthrift::help::serialize_request_envelope::<P, _>("get500", &args) {
            ::std::result::Result::Ok(res) => res,
            ::std::result::Result::Err(err) => return ::futures::future::err(err.into()).boxed(),
        };

        let call = transport
            .call(SERVICE_NAME, SERVICE_METHOD_NAME, request_env, rpc_options)
            .instrument(::tracing::trace_span!("call", method = "Raiser.get500"));

        async move {
            let reply_env = call.await?;

            let de = P::deserializer(reply_env);
            let res = ::fbthrift::help::async_deserialize_response_envelope::<P, crate::errors::raiser::Get500Reader, S>(de).await?;

            let res = match res {
                ::std::result::Result::Ok(res) => res,
                ::std::result::Result::Err(aexn) => {
                    ::std::result::Result::Err(crate::errors::raiser::Get500Error::ApplicationException(aexn))
                }
            };
            res
        }
        .instrument(::tracing::info_span!("stream", method = "Raiser.get500"))
        .boxed()
    }
}

impl<P, T, S> ::fbthrift::help::GetTransport<T> for RaiserImpl<P, T, S>
where
    T: ::fbthrift::Transport,
{
    fn transport(&self) -> &T {
        &self.transport
    }
}

pub trait Raiser: ::std::marker::Send {
    fn doBland(
        &self,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoBlandError>>;

    fn doRaise(
        &self,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoRaiseError>>;

    fn get200(
        &self,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get200Error>>;

    fn get500(
        &self,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get500Error>>;
}

pub trait RaiserExt<T>: Raiser
where
    T: ::fbthrift::Transport,
{
    fn doBland_with_rpc_opts(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoBlandError>>;
    fn doRaise_with_rpc_opts(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoRaiseError>>;
    fn get200_with_rpc_opts(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get200Error>>;
    fn get500_with_rpc_opts(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get500Error>>;

    fn transport(&self) -> &T;
}

struct Args_Raiser_doBland<'a> {
    _phantom: ::std::marker::PhantomData<&'a ()>,
}

impl<'a, P: ::fbthrift::ProtocolWriter> ::fbthrift::Serialize<P> for self::Args_Raiser_doBland<'a> {
    #[inline]
    #[::tracing::instrument(skip_all, level = "trace", name = "serialize_args", fields(method = "Raiser.doBland"))]
    fn write(&self, p: &mut P) {
        p.write_struct_begin("args");
        p.write_field_stop();
        p.write_struct_end();
    }
}

struct Args_Raiser_doRaise<'a> {
    _phantom: ::std::marker::PhantomData<&'a ()>,
}

impl<'a, P: ::fbthrift::ProtocolWriter> ::fbthrift::Serialize<P> for self::Args_Raiser_doRaise<'a> {
    #[inline]
    #[::tracing::instrument(skip_all, level = "trace", name = "serialize_args", fields(method = "Raiser.doRaise"))]
    fn write(&self, p: &mut P) {
        p.write_struct_begin("args");
        p.write_field_stop();
        p.write_struct_end();
    }
}

struct Args_Raiser_get200<'a> {
    _phantom: ::std::marker::PhantomData<&'a ()>,
}

impl<'a, P: ::fbthrift::ProtocolWriter> ::fbthrift::Serialize<P> for self::Args_Raiser_get200<'a> {
    #[inline]
    #[::tracing::instrument(skip_all, level = "trace", name = "serialize_args", fields(method = "Raiser.get200"))]
    fn write(&self, p: &mut P) {
        p.write_struct_begin("args");
        p.write_field_stop();
        p.write_struct_end();
    }
}

struct Args_Raiser_get500<'a> {
    _phantom: ::std::marker::PhantomData<&'a ()>,
}

impl<'a, P: ::fbthrift::ProtocolWriter> ::fbthrift::Serialize<P> for self::Args_Raiser_get500<'a> {
    #[inline]
    #[::tracing::instrument(skip_all, level = "trace", name = "serialize_args", fields(method = "Raiser.get500"))]
    fn write(&self, p: &mut P) {
        p.write_struct_begin("args");
        p.write_field_stop();
        p.write_struct_end();
    }
}

impl<P, T, S> Raiser for RaiserImpl<P, T, S>
where
    P: ::fbthrift::Protocol,
    T: ::fbthrift::Transport,
    P::Frame: ::fbthrift::Framing<DecBuf = ::fbthrift::FramingDecoded<T>>,
    ::fbthrift::ProtocolEncoded<P>: ::fbthrift::BufMutExt<Final = ::fbthrift::FramingEncodedFinal<T>>,
    P::Deserializer: ::std::marker::Send,
    S: ::fbthrift::help::Spawner,
{
    fn doBland(
        &self,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoBlandError>> {
        let rpc_options = T::RpcOptions::default();
        self._doBland_impl(
            rpc_options,
        )
    }
    fn doRaise(
        &self,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoRaiseError>> {
        let rpc_options = T::RpcOptions::default();
        self._doRaise_impl(
            rpc_options,
        )
    }
    fn get200(
        &self,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get200Error>> {
        let rpc_options = T::RpcOptions::default();
        self._get200_impl(
            rpc_options,
        )
    }
    fn get500(
        &self,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get500Error>> {
        let rpc_options = T::RpcOptions::default();
        self._get500_impl(
            rpc_options,
        )
    }
}

impl<P, T, S> RaiserExt<T> for RaiserImpl<P, T, S>
where
    P: ::fbthrift::Protocol,
    T: ::fbthrift::Transport,
    P::Frame: ::fbthrift::Framing<DecBuf = ::fbthrift::FramingDecoded<T>>,
    ::fbthrift::ProtocolEncoded<P>: ::fbthrift::BufMutExt<Final = ::fbthrift::FramingEncodedFinal<T>>,
    P::Deserializer: ::std::marker::Send,
    S: ::fbthrift::help::Spawner,
{
    fn doBland_with_rpc_opts(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoBlandError>> {
        self._doBland_impl(
            rpc_options,
        )
    }
    fn doRaise_with_rpc_opts(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoRaiseError>> {
        self._doRaise_impl(
            rpc_options,
        )
    }
    fn get200_with_rpc_opts(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get200Error>> {
        self._get200_impl(
            rpc_options,
        )
    }
    fn get500_with_rpc_opts(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get500Error>> {
        self._get500_impl(
            rpc_options,
        )
    }

    fn transport(&self) -> &T {
        self.transport()
    }
}

#[allow(deprecated)]
impl<'a, S> Raiser for S
where
    S: ::std::convert::AsRef<dyn Raiser + 'a>,
    S: ::std::marker::Send,
{
    fn doBland(
        &self,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoBlandError>> {
        self.as_ref().doBland(
        )
    }
    fn doRaise(
        &self,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoRaiseError>> {
        self.as_ref().doRaise(
        )
    }
    fn get200(
        &self,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get200Error>> {
        self.as_ref().get200(
        )
    }
    fn get500(
        &self,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get500Error>> {
        self.as_ref().get500(
        )
    }
}

#[allow(deprecated)]
impl<'a, S, T> RaiserExt<T> for S
where
    S: ::std::convert::AsRef<dyn Raiser + 'a> + ::std::convert::AsRef<dyn RaiserExt<T> + 'a>,
    S: ::std::marker::Send + ::fbthrift::help::GetTransport<T>,
    T: ::fbthrift::Transport,
{
    fn doBland_with_rpc_opts(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoBlandError>> {
        <Self as ::std::convert::AsRef<dyn RaiserExt<T>>>::as_ref(self).doBland_with_rpc_opts(
            rpc_options,
        )
    }
    fn doRaise_with_rpc_opts(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<(), crate::errors::raiser::DoRaiseError>> {
        <Self as ::std::convert::AsRef<dyn RaiserExt<T>>>::as_ref(self).doRaise_with_rpc_opts(
            rpc_options,
        )
    }
    fn get200_with_rpc_opts(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get200Error>> {
        <Self as ::std::convert::AsRef<dyn RaiserExt<T>>>::as_ref(self).get200_with_rpc_opts(
            rpc_options,
        )
    }
    fn get500_with_rpc_opts(
        &self,
        rpc_options: T::RpcOptions,
    ) -> ::futures::future::BoxFuture<'static, ::std::result::Result<::std::string::String, crate::errors::raiser::Get500Error>> {
        <Self as ::std::convert::AsRef<dyn RaiserExt<T>>>::as_ref(self).get500_with_rpc_opts(
            rpc_options,
        )
    }

    fn transport(&self) -> &T {
        ::fbthrift::help::GetTransport::transport(self)
    }
}

#[derive(Clone)]
pub struct make_Raiser;

/// To be called by user directly setting up a client. Avoids
/// needing ClientFactory trait in scope, avoids unidiomatic
/// make_Trait name.
///
/// ```
/// # const _: &str = stringify! {
/// use bgs::client::BuckGraphService;
///
/// let protocol = BinaryProtocol::new();
/// let transport = HttpClient::new();
/// let client = <dyn BuckGraphService>::new(protocol, transport);
/// # };
/// ```
impl dyn Raiser {
    pub fn new<P, T>(
        protocol: P,
        transport: T,
    ) -> ::std::sync::Arc<impl Raiser + ::std::marker::Send + ::std::marker::Sync + 'static>
    where
        P: ::fbthrift::Protocol<Frame = T>,
        T: ::fbthrift::Transport,
        P::Deserializer: ::std::marker::Send,
    {
        let spawner = ::fbthrift::help::NoopSpawner;
        Self::with_spawner(protocol, transport, spawner)
    }

    pub fn with_spawner<P, T, S>(
        protocol: P,
        transport: T,
        spawner: S,
    ) -> ::std::sync::Arc<impl Raiser + ::std::marker::Send + ::std::marker::Sync + 'static>
    where
        P: ::fbthrift::Protocol<Frame = T>,
        T: ::fbthrift::Transport,
        P::Deserializer: ::std::marker::Send,
        S: ::fbthrift::help::Spawner,
    {
        let _ = protocol;
        let _ = spawner;
        ::std::sync::Arc::new(RaiserImpl::<P, T, S>::new(transport))
    }
}

impl<T> dyn RaiserExt<T>
where
    T: ::fbthrift::Transport,
{
    pub fn new<P>(
        protocol: P,
        transport: T,
    ) -> ::std::sync::Arc<impl RaiserExt<T> + ::std::marker::Send + ::std::marker::Sync + 'static>
    where
        P: ::fbthrift::Protocol<Frame = T>,
        P::Deserializer: ::std::marker::Send,
    {
        let spawner = ::fbthrift::help::NoopSpawner;
        Self::with_spawner(protocol, transport, spawner)
    }

    pub fn with_spawner<P, S>(
        protocol: P,
        transport: T,
        spawner: S,
    ) -> ::std::sync::Arc<impl RaiserExt<T> + ::std::marker::Send + ::std::marker::Sync + 'static>
    where
        P: ::fbthrift::Protocol<Frame = T>,
        P::Deserializer: ::std::marker::Send,
        S: ::fbthrift::help::Spawner,
    {
        let _ = protocol;
        let _ = spawner;
        ::std::sync::Arc::new(RaiserImpl::<P, T, S>::new(transport))
    }
}

pub type RaiserDynClient = <make_Raiser as ::fbthrift::ClientFactory>::Api;
pub type RaiserClient = ::std::sync::Arc<RaiserDynClient>;

/// The same thing, but to be called from generic contexts where we are
/// working with a type parameter `C: ClientFactory` to produce clients.
impl ::fbthrift::ClientFactory for make_Raiser {
    type Api = dyn Raiser + ::std::marker::Send + ::std::marker::Sync + 'static;

    fn with_spawner<P, T, S>(protocol: P, transport: T, spawner: S) -> ::std::sync::Arc<Self::Api>
    where
        P: ::fbthrift::Protocol<Frame = T>,
        T: ::fbthrift::Transport,
        P::Deserializer: ::std::marker::Send,
        S: ::fbthrift::help::Spawner,
    {
        <dyn Raiser>::with_spawner(protocol, transport, spawner)
    }
}

